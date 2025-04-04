#!/usr/bin/env python
# This is part of the Coding Challenges: https://codingchallenges.fyi/challenges/challenge-cat

import argparse

READ_FROM_STDIN_STRING = "-"

# Initialise the parser
parser = argparse.ArgumentParser("concatenate and print files")
parser.add_argument("filenames", nargs='+', help="filenames of the files to concatenate and print", type=str)
args = parser.parse_args()


for filename in args.filenames:

    if filename != READ_FROM_STDIN_STRING:
        try:
            with open(filename) as file:
                print(file.read(), end="")

        except FileNotFoundError:
            print(f"file {filename} was not found")

        except IsADirectoryError:
            print(f"{filename} is a directory and not a file")

        except:
            print("An exception occurred")

    # Read from stdin
    else:
        # print("stdin reading...")
        while True:
            try:
                print(input(""))
            except KeyboardInterrupt:
                print("")
                exit()
            except:
                break
