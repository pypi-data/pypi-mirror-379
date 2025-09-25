#!/usr/bin/env python3
"""
Main entry point for WhisperingScript command-line interface.
"""

import argparse
import sys

from .automation import WhisperingAutomation


def main():
    """Main entry point for command-line interface"""
    parser = argparse.ArgumentParser(
        description="WhisperingScript - Browser automation for whispering.bradenwong.com",
        prog="whisperingscript"
    )
    parser.add_argument(
        "--stop-method",
        choices=["file", "signal", "time"],
        default="file",
        help="Method to stop recording (default: file)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=30,
        help="Recording duration in seconds for timer method (default: 30)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser in headless mode (default: True)",
    )
    parser.add_argument(
        "--no-headless",
        action="store_true",
        help="Run browser in visible mode (overrides --headless)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    args = parser.parse_args()

    # Handle headless mode
    headless = args.headless and not args.no_headless

    print("WhisperingScript - Browser Automation")
    print("=====================================")
    print("This script automates the whispering.bradenwong.com workflow")
    print(f"Stop method: {args.stop_method}")
    print(f"Headless mode: {headless}")
    if args.stop_method == "time":
        print(f"Recording duration: {args.duration} seconds")
    print()

    # Check if running in terminal for certain stop methods
    if not sys.stdin.isatty() and args.stop_method not in ["file", "signal", "time"]:
        print("Warning: Not running in an interactive terminal.")
        print("Consider using --stop-method file, signal, or time for background operation.")

    try:
        # Create and run automation
        automation = WhisperingAutomation(
            headless=headless,
            stop_method=args.stop_method,
            recording_duration=args.duration,
        )
        result = automation.run()

        if result:
            print(f"\nFinal transcription result: {result}")
            return 0
        else:
            print("\nNo transcription result obtained")
            return 1

    except KeyboardInterrupt:
        print("\n⚠ Automation interrupted by user")
        return 130  # Standard exit code for SIGINT
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
