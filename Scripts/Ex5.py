#!/usr/bin/env python3

import sys
import re
import os
import argparse

# Exercise Sheet 5

# 1. Replacer Tool

parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("-p", "--pattern", default = ",")
parser.add_argument("-r", "--replace", default = ",")
parser.add_argument("-o", "--out")
parser.add_argument("-fo", "--force", action = "store_false")
args = parser.parse_args()

# Assume file is .txt (in sheet is says .ext, typo?)

with open(args.filename, "r") as file_obj:
    content = file_obj.read() #.splitlines()

content = re.sub(args.pattern, args.replace, content)

if args.out:
    if args.out in os.listdir() and args.force:
        print("Error: File already exists. Use True --force to overwrite.")
    else:
        with open(args.filename, "w") as file_obj:
            file_obj.write(content)
else:
    out = re.sub(".txt", "_mod.txt", args.filename)
    with open(out, "w") as file_obj:
        file_obj.write(content)

# 2. Regular Expressions

re.sub("([0-9]{4})-([0-9]{2})-([0-9]{2})", "\\3-\\2-\\1", "2023-10-01")

[(x.group(), x.span()) for x in re.finditer("[0-9]+", "I can count to 100, but not to 1e6")]

[(x.group(), x.span()) for x in re.finditer("[0-9]+.[0-9]+", "1 is not a float, but 2.5 is...")]


# [re.sub("([A-Za-z])([A-Za-z]+)", "\\1", x.lower()).upper() + re.sub("([A-Za-z])([A-Za-z]+)", "\\2", x.lower()) for x in re.findall("[A-Za-z]+", "Testing_this_out")[1:]]
string_to_change = "Testing_this_ouT"
string_to_change
re.findall("[A-Za-z]+", string_to_change)[0].lower() + "".join([x.lower().capitalize() for x in re.findall("[A-Za-z]+", string_to_change)[1:]])

string_to_compress = "acccgtaaaaatc"

multiples = [y for y in [re.findall("[" + x + "]{2,}", string_to_compress) for x in set(string_to_compress)] if len(y) > 0]

for x in multiples:
    x_new = "".join(x)
    string_to_compress = re.sub(x_new, x_new[0] + "[" + str(len(x_new)) + "]", string_to_compress)