import os
import sys
import argparse

def main():
    # Creates the argument parser
    parser = argparse.ArgumentParser(description="Argparse learning CLI tool")

    # Available arguments. All arguments are optional
    parser.add_argument("stuff", nargs="?", help="Does stuff...nothing of importance")

    if sys.argv[1] == "stuff":
        do_stuff()

    args = parser.parse_args()

def do_stuff():
    print("is stuff happening?")
    for i in range(1, 10):
        print(i)

if __name__ == "__main__":
    main()
