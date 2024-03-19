import argparse
import sys
from argparse import ArgumentParser, ArgumentTypeError, RawDescriptionHelpFormatter


def timeout_check(value):
    """Ensure that the timeout is a positive integer."""
    ivalue = int(value)
    if ivalue <= 0:
        raise ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue


def parse_arguments():
    """Parse and validate command line arguments."""
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description="Sherlock: Find Usernames Across Social Networks")
    # Add arguments as defined in the original sherlock.py script
    parser.add_argument("--version", action="version", version="%(prog)s 0.14.3")
    parser.add_argument("--verbose", "-v", "-d", "--debug", action="store_true",
                        help="Display extra debugging information and metrics.")
    # Add other arguments similarly...

    # Return parsed arguments
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    # args can now be used within this script or imported elsewhere
