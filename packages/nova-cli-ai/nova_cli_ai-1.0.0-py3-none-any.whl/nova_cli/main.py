#!/usr/bin/env python3
"""
NOVA CLI - Advanced AI-Powered CLI Assistant
Entry point for the application
"""

import sys
import os

# Add current directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def main():
    """Main entry point for nova-cli command"""
    try:
        # Import your main CLI file
        from NOVA_CLI import main as cli_main
        
        # Run the CLI
        cli_main()
        
    except KeyboardInterrupt:
        print("\n👋 Thanks for using NOVA CLI!")
        sys.exit(0)
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Make sure all required dependencies are installed.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting NOVA CLI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()