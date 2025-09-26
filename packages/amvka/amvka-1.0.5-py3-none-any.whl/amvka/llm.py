"""
LLM integration for converting natural language to shell commands.
"""

import re
import json
from typing import Optional, Dict

try:
    import google.generativeai as genai
except ImportError:
    genai = None

try:
    import openai
except ImportError:
    openai = None

from .utils import print_error, print_info, print_warning
from .environment import EnvironmentDetector


class LLMClient:
    """Client for interacting with LLM APIs."""
    
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.provider = config_manager.get_provider()
        self.api_key = config_manager.get_api_key()
        self.model = config_manager.get_model()
        self.active_model = self.model  # Track actively used model
        self.env_detector = EnvironmentDetector()
        
        if not self.api_key:
            raise ValueError("No API key configured. Run 'amvka config' to set up.")
        
        self._setup_client()
    
    def _setup_client(self):
        """Intelligently setup LLM client with auto-detection and fallbacks."""
        if self.provider == "gemini":
            self._setup_gemini_client()
        elif self.provider == "openai":
            self._setup_openai_client()
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")
    
    def _setup_gemini_client(self):
        """Setup Gemini client with intelligent model detection."""
        if genai is None:
            raise ImportError("google-generativeai package not installed. Run: pip install google-generativeai")
        
        try:
            genai.configure(api_key=self.api_key)
            
            # Try to use the configured model first
            model_name = self._normalize_gemini_model(self.model)
            self.client = genai.GenerativeModel(model_name)
            self.active_model = model_name
            
            # Test the client with a simple request to ensure it works
            self._test_client_connection()
            
        except Exception as e:
            print_warning(f"Primary model '{self.model}' failed, trying fallbacks...")
            self._try_fallback_models("gemini")
    
    def _setup_openai_client(self):
        """Setup OpenAI client with intelligent model detection."""
        if openai is None:
            raise ImportError("openai package not installed. Run: pip install openai")
        
        try:
            self.client = openai.OpenAI(api_key=self.api_key)
            self.active_model = self.model
            
            # Test the client
            self._test_client_connection()
            
        except Exception as e:
            print_warning(f"Primary model '{self.model}' failed, trying fallbacks...")
            self._try_fallback_models("openai")
    
    def _normalize_gemini_model(self, model: str) -> str:
        """Normalize Gemini model names to work with standard API."""
        # Handle various Gemini model formats
        model = model.lower().strip()
        
        # Remove vertex AI prefixes if present
        if "projects/" in model:
            model = model.split("/")[-1]
        
        # Map old/variant names to current ones
        model_mappings = {
            "gemini-1.5-flash-002": "gemini-1.5-flash",
            "gemini-1.5-flash-001": "gemini-1.5-flash", 
            "gemini-1.5-pro-002": "gemini-1.5-pro",
            "gemini-1.5-pro-001": "gemini-1.5-pro",
            "gemini-pro": "gemini-1.0-pro",
            "text-bison": "gemini-1.0-pro",
        }
        
        return model_mappings.get(model, model)
    
    def _try_fallback_models(self, provider: str):
        """Try fallback models if primary fails."""
        fallback_models = self.config_manager.get_fallback_models()
        
        for fallback_model in fallback_models:
            try:
                if provider == "gemini":
                    model_name = self._normalize_gemini_model(fallback_model)
                    self.client = genai.GenerativeModel(model_name)
                    self.active_model = model_name
                else:  # openai
                    self.active_model = fallback_model
                
                self._test_client_connection()
                print_info(f"✅ Successfully connected using fallback model: {self.active_model}")
                return
                
            except Exception:
                continue
        
        raise ValueError(f"Unable to connect with any available {provider} models. Please check your API key and network connection.")
    
    def _test_client_connection(self):
        """Test client connection with a minimal request."""
        try:
            if self.provider == "gemini":
                # Test with a very simple prompt
                test_response = self.client.generate_content("Say 'OK' if you can respond.")
                if not test_response or not test_response.text:
                    raise Exception("No response from model")
            else:  # openai
                # Test with a simple completion
                test_response = self.client.chat.completions.create(
                    model=self.active_model,
                    messages=[{"role": "user", "content": "Say 'OK' if you can respond."}],
                    max_tokens=5
                )
                if not test_response.choices[0].message.content:
                    raise Exception("No response from model")
        except Exception as e:
            raise Exception(f"Client test failed: {str(e)}")
    
    def get_command(self, query: str, context: Dict = None) -> Optional[str]:
        """Intelligently process query - classify intent and respond appropriately."""
        # First classify the query intent
        intent = self._classify_query_intent(query)
        
        if intent == "INFORMATION_REQUEST":
            return self._handle_information_request(query)
        elif intent == "COMMAND_REQUEST":
            return self._generate_command(query, context)
        else:
            # Handle greetings, help, etc. through normal flow
            return self._generate_command(query, context)
    
    def _classify_query_intent(self, query: str) -> str:
        """Classify whether user wants information or a command."""
        classification_prompt = f"""You are an intelligent intent classifier. Classify this user query into ONE of these categories:

INFORMATION_REQUEST: User wants to know information/facts (like "who is PM of India", "what is the weather", "what time is it")
COMMAND_REQUEST: User wants to perform a system action (like "list files", "create folder", "check processes", "install package")
OTHER: Greetings, help requests, unclear queries

Rules:
- Questions starting with "who", "what", "when", "where", "how much", "how many" are usually INFORMATION_REQUEST
- Requests to "show", "list", "create", "delete", "install", "run", "execute" are usually COMMAND_REQUEST
- Consider context - "show me the weather" = INFORMATION_REQUEST, "show me files" = COMMAND_REQUEST

User query: "{query}"

Classification:"""

        try:
            if self.provider == "gemini":
                response = self.client.generate_content(classification_prompt)
                classification = response.text.strip()
            elif self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": classification_prompt}],
                    max_tokens=50,
                    temperature=0.1
                )
                classification = response.choices[0].message.content.strip()
            
            if "INFORMATION_REQUEST" in classification:
                return "INFORMATION_REQUEST"
            elif "COMMAND_REQUEST" in classification:
                return "COMMAND_REQUEST"
            else:
                return "OTHER"
                
        except Exception as e:
            # Smart error handling - don't show technical errors to users
            error_msg = str(e)
            if "404" in error_msg or "not found" in error_msg.lower():
                print_info("🔧 Adapting to available models...")
            elif "api key" in error_msg.lower() or "unauthorized" in error_msg.lower():
                print_error("❌ API key issue. Run 'amvka config' to reconfigure.")
            else:
                print_info("🤖 Processing your request...")
            return "COMMAND_REQUEST"  # Default to command if classification fails
    
    def _handle_information_request(self, query: str) -> Optional[str]:
        """Handle information requests by providing answers directly."""
        info_prompt = f"""You are a helpful assistant that provides direct answers to questions. 

The user is asking for information, not a command. Provide a helpful, concise answer.

If you don't know the specific current information (like current PM, weather, etc.), respond with:
"SEARCH_NEEDED: [brief explanation of what current info is needed]"

User question: {query}

Answer:"""

        try:
            if self.provider == "gemini":
                response = self.client.generate_content(info_prompt)
                answer = response.text.strip()
            elif self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": info_prompt}],
                    max_tokens=200,
                    temperature=0.3
                )
                answer = response.choices[0].message.content.strip()
            
            if "SEARCH_NEEDED:" in answer:
                explanation = answer.replace("SEARCH_NEEDED:", "").strip()
                print_info(f"I need to look up current information: {explanation}")
                print_info("Let me search for that information for you...")
                return self._generate_search_command(query)
            else:
                print_info(f"💡 {answer}")
                return None  # No command needed, answer provided
                
        except Exception as e:
            print_error(f"Error getting information: {e}")
            return None
    
    def _generate_search_command(self, query: str) -> Optional[str]:
        """Generate a search command for information queries."""
        env_context = self.env_detector.get_environment_context()
        
        if env_context["os"] == "Windows":
            search_url = query.replace(" ", "+")
            return f'Start-Process "https://www.google.com/search?q={search_url}"'
        else:
            search_url = query.replace(" ", "+")
            return f'open "https://www.google.com/search?q={search_url}"'
    
    def _generate_command(self, query: str, context: Dict = None) -> Optional[str]:
        """Generate shell command using the original logic."""
        prompt = self._build_prompt(query, context)
        
        try:
            if self.provider == "gemini":
                response = self._call_gemini(prompt)
            elif self.provider == "openai":
                response = self._call_openai(prompt)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
            
            return self._extract_command(response)
        
        except Exception as e:
            # Smart error handling with user-friendly messages
            error_msg = str(e)
            if "404" in error_msg or "not found" in error_msg.lower():
                print_info("🔄 Model unavailable, trying alternatives...")
                return self._handle_model_fallback(query, context)
            elif "api key" in error_msg.lower() or "unauthorized" in error_msg.lower():
                print_error("🔑 API authentication failed. Please run 'amvka config' to update your credentials.")
            elif "rate limit" in error_msg.lower() or "quota" in error_msg.lower():
                print_warning("⏳ Rate limit reached. Please wait a moment and try again.")
            else:
                print_info(f"🤖 Temporary issue connecting to {self.provider}. Trying backup approach...")
                return self._handle_model_fallback(query, context)
            return None
    
    def _handle_model_fallback(self, query: str, context: Dict = None) -> Optional[str]:
        """Handle model fallback gracefully."""
        try:
            # Reinitialize with fallback
            self._try_fallback_models(self.provider)
            return self._generate_command(query, context)
        except Exception:
            print_warning("⚠️  All models temporarily unavailable. Please check your internet connection and API key.")
            return None
    
    def _build_prompt(self, query: str, context: Dict = None) -> str:
        """Build the prompt for the LLM with environment awareness and context."""
        env_context = self.env_detector.get_environment_context()
        
        os_name = env_context["os"]
        shell = env_context["shell"]
        supported_commands = env_context["supported_commands"]
        command_examples = env_context["command_examples"]
        
        # Build examples based on current environment
        examples_text = "\n".join([
            f'"{intent}" → {cmd}' 
            for intent, cmd in command_examples.items()
        ])
        
        # Build supported commands list
        supported_text = ", ".join(supported_commands[:15])  # Limit to avoid token overflow
        if len(supported_commands) > 15:
            supported_text += f" (and {len(supported_commands) - 15} more)"
        
        # Add context information if provided
        context_info = ""
        if context:
            if "files" in context:
                files_list = ", ".join([f["path"] for f in context["files"][:5]])
                context_info += f"\nAvailable files in directory: {files_list}"
            if "project_type" in context:
                context_info += f"\nProject type: {context['project_type']}"
        
        if os_name == "Windows":
            if shell == "powershell":
                prompt = f"""You are an intelligent AI assistant that converts natural language requests into PowerShell commands for Windows systems. You are SMART and can handle ANY request.

CURRENT ENVIRONMENT:
- Operating System: {os_name}
- Shell: {shell.title()}
- Available Commands: {supported_text}{context_info}

🎯 INTELLIGENT BEHAVIOR - HANDLE ALL REQUESTS:
- Simple greetings ("hi", "hello") → respond with "CONVERSATIONAL_INPUT"
- Help requests ("what can you do", "help") → respond with "HELP_REQUEST"  
- Questions about information ("who is PM of India", "what is the weather") → create appropriate commands to get that info
- File operations ("list files", "create file") → generate correct PowerShell commands
- System queries ("check memory", "show processes") → generate system commands
- Web searches ("search for X", "look up Y") → create search commands
- ANY other actionable request → generate the appropriate PowerShell command

🛡️ SAFETY RULES:
- If request is destructive/dangerous → respond with "UNSAFE_COMMAND"
- Only respond with clean PowerShell commands (no explanations/markdown)
- Use proper PowerShell syntax and cmdlets

💡 INTELLIGENCE EXAMPLES:
- "who is PM of India" → Start-Process "https://www.google.com/search?q=who+is+prime+minister+of+india"
- "what's the weather" → Start-Process "https://www.google.com/search?q=weather"  
- "show me python files" → Get-ChildItem -Filter *.py
- "check memory usage" → Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10

EXAMPLES FOR YOUR ENVIRONMENT:
{examples_text}

User request: {query}

Response:"""
            
            else:  # CMD
                prompt = f"""You are an intelligent AI assistant that converts natural language requests into CMD commands for Windows systems. You are SMART and can handle ANY request.

CURRENT ENVIRONMENT:
- Operating System: {os_name}
- Shell: Command Prompt (CMD)
- Available Commands: {supported_text}{context_info}

🎯 INTELLIGENT BEHAVIOR - HANDLE ALL REQUESTS:
- Simple greetings ("hi", "hello") → respond with "CONVERSATIONAL_INPUT"
- Help requests ("what can you do", "help") → respond with "HELP_REQUEST"  
- Questions about information ("who is PM of India", "what is the weather") → create appropriate commands to get that info
- File operations ("list files", "create file") → generate correct CMD commands
- System queries ("check memory", "show processes") → generate system commands
- Web searches ("search for X", "look up Y") → create search commands
- ANY other actionable request → generate the appropriate CMD command

🛡️ SAFETY RULES:
- If request is destructive/dangerous → respond with "UNSAFE_COMMAND"
- Only respond with clean CMD commands (no explanations/markdown)
- Use proper CMD syntax

💡 INTELLIGENCE EXAMPLES:
- "who is PM of India" → start https://www.google.com/search?q=who+is+prime+minister+of+india
- "what's the weather" → start https://www.google.com/search?q=weather
- "show me python files" → dir *.py
- "check running processes" → tasklist

EXAMPLES FOR YOUR ENVIRONMENT:
{examples_text}

User request: {query}

Response:"""
        
        else:  # Linux/Unix/Mac
            prompt = f"""You are an intelligent AI assistant that converts natural language requests into {shell} commands for {os_name} systems. You are SMART and can handle ANY request.

CURRENT ENVIRONMENT:
- Operating System: {os_name}
- Shell: {shell.title()}
- Available Commands: {supported_text}{context_info}

🎯 INTELLIGENT BEHAVIOR - HANDLE ALL REQUESTS:
- Simple greetings ("hi", "hello") → respond with "CONVERSATIONAL_INPUT"
- Help requests ("what can you do", "help") → respond with "HELP_REQUEST"  
- Questions about information ("who is PM of India", "what is the weather") → create appropriate commands to get that info
- File operations ("list files", "create file") → generate correct {shell} commands
- System queries ("check memory", "show processes") → generate system commands
- Web searches ("search for X", "look up Y") → create search commands
- ANY other actionable request → generate the appropriate {shell} command

🛡️ SAFETY RULES:
- If request is destructive/dangerous → respond with "UNSAFE_COMMAND"
- Only respond with clean {shell} commands (no explanations/markdown)
- Use proper {shell} syntax

💡 INTELLIGENCE EXAMPLES:
- "who is PM of India" → curl -s "https://www.google.com/search?q=who+is+prime+minister+of+india" || open "https://www.google.com/search?q=who+is+prime+minister+of+india"
- "what's the weather" → curl -s "wttr.in" || open "https://www.google.com/search?q=weather"
- "show me python files" → find . -name "*.py" -type f
- "check memory usage" → free -h || top -l 1 | head -n 10

EXAMPLES FOR YOUR ENVIRONMENT:
{examples_text}

User request: {query}

Response:"""
        
        return prompt
    
    def _call_gemini(self, prompt: str) -> str:
        """Call Gemini API with intelligent error handling."""
        try:
            response = self.client.generate_content(prompt)
            if response and response.text:
                return response.text
            else:
                raise Exception("Empty response from Gemini")
        except Exception as e:
            # Try to recover with a different approach
            if "404" in str(e) or "not found" in str(e).lower():
                print_warning(f"Model '{self.active_model}' not available, trying alternative...")
                return self._retry_with_fallback(prompt, "gemini")
            else:
                raise e
    
    def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API with intelligent error handling."""
        try:
            response = self.client.chat.completions.create(
                model=self.active_model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.1
            )
            return response.choices[0].message.content
        except Exception as e:
            # Try to recover with a different model
            if "model" in str(e).lower() and ("not found" in str(e).lower() or "does not exist" in str(e).lower()):
                print_warning(f"Model '{self.active_model}' not available, trying alternative...")
                return self._retry_with_fallback(prompt, "openai")
            else:
                raise e
    
    def _retry_with_fallback(self, prompt: str, provider: str) -> str:
        """Retry request with fallback models."""
        fallbacks = self.config_manager.get_fallback_models()
        
        for fallback in fallbacks:
            try:
                if provider == "gemini":
                    fallback_normalized = self._normalize_gemini_model(fallback)
                    temp_client = genai.GenerativeModel(fallback_normalized)
                    response = temp_client.generate_content(prompt)
                    if response and response.text:
                        # Update active model on success
                        self.client = temp_client
                        self.active_model = fallback_normalized
                        print_info(f"✅ Switched to working model: {self.active_model}")
                        return response.text
                else:  # openai
                    response = self.client.chat.completions.create(
                        model=fallback,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=100,
                        temperature=0.1
                    )
                    # Update active model on success
                    self.active_model = fallback
                    print_info(f"✅ Switched to working model: {self.active_model}")
                    return response.choices[0].message.content
            except Exception:
                continue
        
        raise Exception(f"All {provider} models failed. Please check your API key and try again.")
    
    def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.1
        )
        return response.choices[0].message.content
    
    def _extract_command(self, response: str) -> Optional[str]:
        """Extract command from LLM response with intelligent handling of different response types."""
        if not response:
            return None
        
        # Clean up the response
        command = response.strip()
        
        # Handle different response types
        if "CONVERSATIONAL_INPUT" in command:
            print_info("Hello! I'm amvka, your AI command assistant. 🎯 No more memorizing commands - just tell me what you want to do and I'll give you the exact command!")
            return None
        
        if "HELP_REQUEST" in command:
            print_info("""🚀 No more memorizing commands! I'm amvka, your AI command assistant.

Just tell me what you want to do in plain English, and I'll give you the exact command:

💬 "Show me all Python files in this folder"
💬 "Check if Docker is running"
💬 "Create a backup of this directory"
💬 "Find large files taking up space"
💬 "Kill the process using port 3000"
💬 "Install the packages from requirements.txt"
💬 "Show system memory usage"
💬 "Connect to my database"

🎯 No syntax to remember, no manual pages to read - just describe your goal naturally!""")
            return None
        
        if "NEEDS_CLARIFICATION:" in command:
            clarification = command.replace("NEEDS_CLARIFICATION:", "").strip()
            print_info(f"I need more information: {clarification}")
            return None
        
        # Check for unsafe command marker
        if "UNSAFE_COMMAND" in command:
            print_warning("The requested operation was deemed unsafe and will not be executed.")
            return None
        
        # Remove common markdown formatting
        command = re.sub(r'^```.*?\n', '', command)
        command = re.sub(r'\n```$', '', command)
        command = re.sub(r'^`(.*)`$', r'\1', command)
        
        # Remove any explanation text (keep only the first line that looks like a command)
        lines = command.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('//'):
                # Validate command against current environment
                if self._is_command_compatible(line):
                    # Basic safety check
                    if self._is_safe_command(line):
                        return line
                    else:
                        print_warning("Command contains potentially dangerous operations and will not be executed.")
                        return None
                else:
                    print_warning(f"Command '{line}' is not compatible with current environment ({self.env_detector.shell_info['shell']} on {self.env_detector.os_type}).")
                    return None
        
        return None
    
    def _is_command_compatible(self, command: str) -> bool:
        """Check if command is compatible with current environment."""
        # Extract the main command (first word)
        main_command = command.split()[0] if command.split() else ""
        
        # Check if the command is in our database and supported
        if self.env_detector.is_command_available(main_command):
            return True
        
        # For compound commands or commands with paths, do basic validation
        env_context = self.env_detector.get_environment_context()
        os_name = env_context["os"]
        shell = env_context["shell"]
        
        # PowerShell specific checks
        if shell == "powershell":
            # Check for PowerShell cmdlet pattern (Verb-Noun)
            if re.match(r'^[A-Z][a-z]+-[A-Z][a-zA-Z]*', main_command):
                return True
            # Check for common PowerShell commands
            ps_commands = ["cd", "ls", "dir", "cat", "echo", "mkdir"]
            if main_command.lower() in ps_commands:
                return True
        
        # CMD specific checks
        elif shell == "cmd":
            cmd_commands = ["dir", "cd", "copy", "del", "mkdir", "rmdir", "echo", "type", "cls"]
            if main_command.lower() in cmd_commands:
                return True
        
        # Unix/Linux shell checks
        else:
            unix_commands = ["ls", "cd", "cp", "mv", "rm", "mkdir", "rmdir", "echo", "cat", "grep", "find", "pwd"]
            if main_command.lower() in unix_commands:
                return True
        
        return False
    
    def _is_safe_command(self, command: str) -> bool:
        """Basic safety check for commands with environment awareness."""
        env_context = self.env_detector.get_environment_context()
        os_name = env_context["os"]
        shell = env_context["shell"]
        
        # List of dangerous command patterns
        dangerous_patterns = []
        
        if os_name == "Windows":
            # Windows PowerShell and CMD dangerous patterns
            dangerous_patterns = [
                r'\bRemove-Item\s+.*-Recurse.*-Force',  # Remove-Item with force and recurse
                r'\brd\s+/s\s+/q\s+c:\\',  # rd command on C drive
                r'\bdel\s+/s\s+/q\s+c:\\',  # del command on C drive
                r'\bformat\s+c:',  # format C drive
                r'\bshutdown\s+',  # shutdown command
                r'\brestart-computer',  # restart computer
                r'\bstop-computer',  # stop computer
                r'\bremove-item\s+.*\$env:systemroot',  # remove system files
                r'\bget-process.*stop-process.*-force',  # aggressive process killing
                r'\bstop-process.*-name.*-force',  # force stop processes
                r'\binvoke-expression.*download',  # downloading and executing scripts
                r'\biex.*download',  # IEX download shorthand
                r'\bset-executionpolicy\s+unrestricted',  # unrestricted execution policy
                r'\brm\s+-rf\s+.*\\',  # rm -rf on Windows (if using PowerShell with Unix aliases)
            ]
        else:
            # Linux/Unix dangerous patterns
            dangerous_patterns = [
                r'\brm\s+-rf\s+/',  # rm -rf /
                r'\brm\s+-rf\s+\*',  # rm -rf *
                r'\bdd\s+if=',  # dd commands
                r':\(\)\{.*\}:',  # fork bomb
                r'sudo\s+rm',  # sudo rm
                r'>\s*/dev/sd[a-z]',  # writing to disk devices
                r'mkfs\.',  # filesystem formatting
                r'fdisk',  # disk partitioning
                r'shutdown',  # system shutdown
                r'reboot',  # system reboot
                r'halt',  # system halt
                r'init\s+0',  # init 0
                r'init\s+6',  # init 6
                r'killall',  # kill all processes
                r'pkill.*-9',  # aggressive process killing
            ]
        
        command_lower = command.lower()
        
        for pattern in dangerous_patterns:
            if re.search(pattern, command_lower):
                return False
        
        return True