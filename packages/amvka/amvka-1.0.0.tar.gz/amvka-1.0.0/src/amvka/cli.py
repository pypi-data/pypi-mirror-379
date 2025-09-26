#!/usr/bin/env python3
"""
Amvka CLI - Main entry point for the amvka command.
"""

import sys
import argparse
from .config import ConfigManager
from .llm import LLMClient
from .executor import CommandExecutor
from .conversation import ConversationManager
from .utils import print_error, print_success, print_info


def main():
    """Main entry point for the amvka CLI."""
    if len(sys.argv) > 1 and sys.argv[1] == "config":
        handle_config_command()
        return
    
    parser = argparse.ArgumentParser(
        description="Amvka - Convert natural language to shell commands using AI",
        prog="amvka",
        add_help=False
    )
    
    parser.add_argument("--yes", "-y", action="store_true", help="Auto-confirm command execution")
    parser.add_argument("--dry-run", action="store_true", help="Show command without executing")
    parser.add_argument("--version", "-v", action="store_true", help="Show version information")
    parser.add_argument("--help", "-h", action="store_true", help="Show help message")
    
    args, remaining = parser.parse_known_args()
    
    if args.version:
        print("amvka 1.0.0")
        return
    
    if args.help or (not remaining and len(sys.argv) == 1):
        show_help()
        return
    
    if not remaining:
        show_help()
        return
    
    query = " ".join(remaining)
    
    try:
        config_manager = ConfigManager()
        
        if not config_manager.is_configured():
            print_info("First time setup required. Let's configure your API key.")
            config_manager.setup_initial_config()
        
        llm_client = LLMClient(config_manager)
        executor = CommandExecutor()
        conversation_manager = ConversationManager(llm_client, executor)
        
        if args.dry_run:
            # For dry run, just show what would be executed
            print_info("DRY RUN MODE - Commands will be shown but not executed")
            conversation_manager.dry_run = True
        
        # Use conversation manager for intelligent processing
        success = conversation_manager.process_query(query, args.yes)
        
    except KeyboardInterrupt:
        print_info("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print_error(f"Error: {e}")
        sys.exit(1)


def handle_config_command():
    """Handle config command."""
    parser = argparse.ArgumentParser(
        description="Configure Amvka settings",
        prog="amvka config"
    )
    parser.add_argument("--reset", action="store_true", help="Reset configuration")
    parser.add_argument("--show", action="store_true", help="Show current configuration")
    
    args = parser.parse_args(sys.argv[2:])
    config_manager = ConfigManager()
    
    if args.show:
        config_manager.show_config()
    elif args.reset:
        config_manager.reset_config()
        print_success("Configuration reset successfully.")
    else:
        config_manager.setup_initial_config()
        print_success("Configuration updated successfully.")


def show_help():
    """Show help message."""
    print("""usage: amvka [OPTIONS] QUERY
       amvka config [--show|--reset]

Amvka - Convert natural language to shell commands using AI

OPTIONS:
    -y, --yes        Auto-confirm command execution
    --dry-run        Show command without executing
    -v, --version    Show version information
    -h, --help       Show this help message

COMMANDS:
    config           Configure API settings
      --show         Show current configuration
      --reset        Reset configuration

EXAMPLES:
    amvka show files here
    amvka create a new file called test.txt
    amvka --dry-run find all Python files
    amvka config""")


if __name__ == "__main__":
    main()