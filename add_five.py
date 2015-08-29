#!/usr/bin/env python

## This script is supposed to add 5 to whatever number the user supplies

import sys

# Make sure user provided a command line argument
if len(sys.argv) != 2:
    sys.stderr.write("usage: python add_five.py <number>\n")
    sys.exit()

user_input = sys.argv[1]
print(user_input + 5)
