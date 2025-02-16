"""
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
"""

import sys
import calc

def main():
    """
    Main function to handle command line arguments and perform addition
    """
    if len(sys.argv) != 3:
        print("\nYou entered {} value(s).".format(len(sys.argv) - 1))
        print("\nUsage: 'add2vals X Y' where X and Y are individual values.")
        print("       If add2vals is not in your path, usage is './add2vals X Y'.")
        print("       If unbundled, usage is 'python add2vals.py X Y'.\n")
        sys.exit(1)

    arg1, arg2 = sys.argv[1], sys.argv[2]

    try:
        result = calc.add2(arg1, arg2)
        print("\nThe result is: {}\n".format(result))
        sys.exit(0)
    except Exception as e:
        print("\nError: {}\n".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
