"""
Main entry point for cypherseed when run as a module.

This module allows cypherseed to be executed as:
- python -m cypherseed
- cypherseed (when installed via pip)
"""

import sys
from .cli import main

if __name__ == '__main__':
    # handle keyboard interrupt gracefully
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)