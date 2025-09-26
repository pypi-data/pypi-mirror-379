"""
Configuration management for Amvka.
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional

from .utils import get_home_config_dir, print_error, print_info, print_success, safe_input


class ConfigManager:
    """Manages configuration for Amvka CLI."""
    
    def __init__(self):
        self.config_dir = get_home_config_dir()
        self.config_file = os.path.join(self.config_dir, "config.json")
        self._config = None
    
    def load_config(self) -> Dict:
        """Load configuration from file."""
        if self._config is not None:
            return self._config
        
        if not os.path.exists(self.config_file):
            self._config = {}
            return self._config
        
        try:
            with open(self.config_file, 'r') as f:
                self._config = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print_error(f"Error loading config: {e}")
            self._config = {}
        
        return self._config
    
    def save_config(self, config: Dict):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            self._config = config
        except IOError as e:
            print_error(f"Error saving config: {e}")
            raise
    
    def is_configured(self) -> bool:
        """Check if the tool is properly configured."""
        config = self.load_config()
        return bool(config.get("api_key") and config.get("provider"))
    
    def get_api_key(self) -> Optional[str]:
        """Get the API key from config."""
        config = self.load_config()
        return config.get("api_key")
    
    def get_provider(self) -> Optional[str]:
        """Get the LLM provider from config."""
        config = self.load_config()
        return config.get("provider", "gemini")
    
    def setup_initial_config(self):
        """Setup initial configuration interactively."""
        print_info("Setting up Amvka configuration...")
        print_info("Amvka supports Google Gemini and OpenAI APIs.")
        
        # Choose provider
        print_info("\nAvailable providers:")
        print("1. Google Gemini (recommended)")
        print("2. OpenAI")
        
        while True:
            choice = safe_input("Choose provider (1 or 2): ", "1")
            if choice in ["1", "2"]:
                break
            print_error("Please enter 1 or 2")
        
        provider = "gemini" if choice == "1" else "openai"
        
        # Get API key
        if provider == "gemini":
            print_info("\nTo get a Gemini API key:")
            print_info("1. Go to https://aistudio.google.com/app/apikey")
            print_info("2. Sign in with your Google account")
            print_info("3. Create a new API key")
            api_key = safe_input("\nEnter your Gemini API key: ")
        else:
            print_info("\nTo get an OpenAI API key:")
            print_info("1. Go to https://platform.openai.com/api-keys")
            print_info("2. Sign in to your OpenAI account")
            print_info("3. Create a new API key")
            api_key = safe_input("\nEnter your OpenAI API key: ")
        
        if not api_key:
            print_error("API key is required!")
            return
        
        # Additional settings
        config = {
            "provider": provider,
            "api_key": api_key,
            "model": "gemini-1.5-flash" if provider == "gemini" else "gpt-3.5-turbo",
            "safety_confirmation": True
        }
        
        self.save_config(config)
        print_success(f"Configuration saved successfully using {provider.title()}!")
    
    def show_config(self):
        """Show current configuration (without showing API key)."""
        config = self.load_config()
        
        if not config:
            print_info("No configuration found. Run 'amvka config' to set up.")
            return
        
        print_info("Current configuration:")
        print(f"Provider: {config.get('provider', 'Not set')}")
        print(f"Model: {config.get('model', 'Not set')}")
        print(f"API Key: {'*' * 8}...{config.get('api_key', '')[-4:] if config.get('api_key') else 'Not set'}")
        print(f"Safety confirmation: {config.get('safety_confirmation', True)}")
    
    def reset_config(self):
        """Reset configuration by removing the config file."""
        if os.path.exists(self.config_file):
            os.remove(self.config_file)
            self._config = None
        else:
            print_info("No configuration file found to reset.")
    
    def get_model(self) -> str:
        """Get the model name from config."""
        config = self.load_config()
        provider = self.get_provider()
        
        if provider == "gemini":
            return config.get("model", "gemini-1.5-flash")
        else:
            return config.get("model", "gpt-3.5-turbo")