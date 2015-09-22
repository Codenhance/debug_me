#!/usr/bin/env python

## This script collects info about a user's computing
## environment, then writes it to a .tsv file

import sys

print("Hi there. Please answer a few questions to help me build your profile."
github_username = raw_input("What's your GitHub username? ")
boot_os = raw_input("What is your boot OS? ")
use_virtualbox = raw_input("Do you use VirtualBox? ")
text_editor = raw_input(Which text editor do you use? ")
new_to_python = raw_input("Are you new to Python? ")
new_to_programming = raw_input("Are you new to programming in general? ")
print("\nThanks. Now I'll write your profile to a file.")
filename = raw_input("What should I call it? ")

with open(filename, 'w') as outfile
    outfile.write("GitHub username\t%s\n" % github_username)
    outfile.write("Boot OS\t%s\n" % boot_os)
    outfile.write("Use Virtualbox\t%s\n" % use_virtualbox)
    outfile.write("Text Editor\t%s\n" % text_editor)
    outfile.write("New to Python?\t%s\n" % new_to_python)
    outfile.write("New to Programming?\t%s\n"  new_t_programming)

