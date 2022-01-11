import os
import argparse

def main():
    # Creates the argument parser
    parser = argparse.ArgumentParser(description="Argparse learning CLI tool")

    # Available arguments. All arguments are optional
    parser.add_argument("stuff", nargs="?", help="Helps create Okta groups used as Google groups")
    
    if sys.argv[1] == "stuff":
        do_stuff()
        
    args = parser.parse)args()

def do_stuff():
    print("is stuff happening?")
    for i in range(1, 10):
        print(i)
        
if __name__ == "__main__":
    main()
