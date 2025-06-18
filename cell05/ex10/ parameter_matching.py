#!/usr/bin/env python3
import sys

# Check if there is exactly one argument passed to the script
if len(sys.argv) != 2:
    print("none")
else:
    # The argument passed is stored in sys.argv[1]
    param = sys.argv[1]

    # Prompt the user to enter a word
    word = input("What was the parameter? ")

    # Compare the entered word with the parameter
    if word == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
