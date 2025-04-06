#!/usr/bin/env python
# This is part of the Coding Challenges: https://codingchallenges.fyi/challenges/challenge-cat

import argparse
import textwrap
import sys
import signal

# constants
READ_FROM_STDIN_STRING = "-"
LEFT_PADDING_SIZE = 6

# globals
g_lineCounter = 1       # Line count starts from 1
g_endChar = "\n"        # Intitial end char is new line so that the numbering of lines begins properly

def printFileTextWithLineNumbers(text):
    global g_lineCounter
    global g_endChar
    file_line_counter = 1
    lines = text.split("\n")
    for line in lines:
        if g_endChar == "\n":
            line = f"{str(g_lineCounter).rjust(LEFT_PADDING_SIZE)}  {line}" # Add line counter prefix only if there was a new line
            g_lineCounter += 1  # Increment the global line counter (for next line)

        g_endChar = "" if file_line_counter == len(lines) else "\n" # Calculate new end char
        file_line_counter += 1

        print(line, end=g_endChar) # Print line

def printFileText(text):
    print(text, end="")

def stdinMode():
    while True:
        try:
            print(input(""))
        except KeyboardInterrupt:
            print("")
            exit()
        except:
            break

def filenameMode(filename, args):
    try:
        with open(filename) as file:
            if args.number:
                printFileTextWithLineNumbers(file.read())
            else:
                printFileText(file.read())

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
    parser.add_argument("-n", "--number", action='store_true', help="number the output lines")
    args = parser.parse_args()


    # If zero filename args where provided then go to stdin mode
    if not args.filenames:
        stdinMode()
    else:
        for filename in args.filenames:
            if filename != READ_FROM_STDIN_STRING:
                filenameMode(filename, args)
            else:
                stdinMode()


if __name__ == "__main__":
    # Prevent broken pipe errors when piping to commands like `head`
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()


# TODO:
#   - add number lines in stdin stdinMode (tests: 19, 20)
