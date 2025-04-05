#!/usr/bin/env python
# This is part of the Coding Challenges: https://codingchallenges.fyi/challenges/challenge-cat

import argparse

READ_FROM_STDIN_STRING = "-"

def stdinMode():
    while True:
        try:
            print(input(""))
        except KeyboardInterrupt:
            print("")
            exit()
        except:
            break

def filenameMode(filename):
    try:
        with open(filename) as file:
            print(file.read(), end="")

    except FileNotFoundError:
        print(f"file {filename} was not found")

    except IsADirectoryError:
        print(f"{filename} is a directory and not a file")

    except:
        print("an error occurred")


def main(args=None):
    # Initialise the parser
    parser = argparse.ArgumentParser("concatenate and print files")
    parser.add_argument("filenames", nargs='*', help="filenames of the files to concatenate and print", type=str)
    args = parser.parse_args()

    # if zero filename args where provided then go to stdin mode
    if not args.filenames:
        stdinMode()
    else:
        for filename in args.filenames:
            if filename != READ_FROM_STDIN_STRING:
                filenameMode(filename)
            else:
                stdinMode()


if __name__ == "__main__":
    main()
