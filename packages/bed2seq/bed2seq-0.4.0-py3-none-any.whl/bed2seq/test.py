#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--myarg", nargs='?', type=str)
args = parser.parse_args()
print(args)

