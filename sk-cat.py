#!/usr/bin/env python
# This is part of the Coding Challenges: https://codingchallenges.fyi/challenges/challenge-cat

import argparse

parser = argparse.ArgumentParser("concatenate and print files")
parser.add_argument("filenames", nargs='+', help="filenames of the files to concatenate and print", type=str)
args = parser.parse_args()
for filename in args.filenames:
    print(f'Processing file: {filename}')
    # Add your file processing code here
