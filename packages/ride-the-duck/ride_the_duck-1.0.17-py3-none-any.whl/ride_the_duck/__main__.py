#!/usr/bin/env python3
"""
Entry point for the ride-the-duck package.
This allows the package to be run with:
- python -m ride_the_duck
- ride-the-duck (after pip install)
- RTD (after pip install)
"""

def console_entry():
    """Entry point for console commands (ride-the-duck, RTD)."""
    import sys
    try:
        from .mainGame import main as game_main
        game_main()
    except ImportError as e:
        if "termios" in str(e):
            print("Error importing mainGame: No module named 'termios'")
            print("This error occurs on Windows. The game should work, but some features may be limited.")
            print("If you see this error and the game does not start, please update to the latest version.")
        else:
            print(f"Error importing mainGame: {e}")
            print("Please ensure the package is properly installed.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        sys.exit(0)
    except (RuntimeError, ValueError) as e:
        print(f"Error running game: {e}")
        sys.exit(1)

def main():
    """Main entry point when called as python -m ride_the_duck."""
    console_entry()

if __name__ == "__main__":
    main()