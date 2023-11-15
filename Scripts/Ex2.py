#!/usr/bin/env python3

# Exercise Sheet 2

import sys
import re

# 1. Summary

# From lecture
with open("Desktop/MSc. Data Science/iris.num.only.csv", "r") as file_obj:
  for line in file_obj:
    line = line.rstrip()
    print(line)

# Alternatively
with open("Desktop/MSc. Data Science/iris.num.only.csv", "r") as file_obj:
   content = file_obj.read().splitlines() 

rows = content[1:]

header = content[0].split(",")
rows = [i.split(",") for i in rows]
rows = [[float(j) for j in i[:]] for i in rows]

with open("Desktop/MSc. Data Science/iris.num.only.summary.csv" , "w") as file_out:
  
  print("feature", "min", "max", "mean", "median", "variance", sep = ",", file = file_out)
  
  for i in range(len(header)):

    values = [value[i] for value in rows]
    mean = sum(values)/len(values)
    values.sort()
    median = values[int(len(values) / 2)] # doesn't account for even number sized population
    variance = sum([(value - mean) ** 2 for value in values]) / (len(values) - 1)

    print(header[i], min(values), max(values), mean, median, variance, sep = ",", file = file_out)

# 2. GroupBy

with open("Desktop/MSc. Data Science/groupby_example.csv", "r") as file_obj:
   content = file_obj.read().splitlines() 

header = content[:1]
rows = content[1:]

header = [i.split(",") for i in header][0]
rows = [i.split(",") for i in rows]

# group_col = [header[j] for j in range(len(header)) if [i == "col1" for i in header][j]] # don't need to know name, just index
gcol = header.index(sys.argv[1])
acol = header.index(sys.argv[2])

op = {"min": lambda x: min(x),
      "max": lambda x: max(x),
      "mean": lambda x: sum(x) / len(x),
      "sum": lambda x: sum(x)}


gcol_vals = set([row[gcol] for row in rows])

print(header)
for i in gcol_vals:
  acol_vals = [int(rows[j][acol]) for j in range(len(rows)) if [row[gcol] == i for row in rows][j]]
  print(i, op[sys.argv[3]](acol_vals), sep = ",")

# 3. Palindrome detector

with open("Desktop/MSc. Data Science/palindromes_example.txt", "r") as file_obj:
   content = file_obj.read()

content = content.lower()
content = re.sub(r"\n+", " ", content)
content = re.sub(r"\s+", " ", content)
content = re.sub(r"[^a-z ]+", "", content).split()

fwd = [i[:int(len(i)/2) + 1] for i in content]
bwd = [i[int(len(i)/2):][::-1] for i in content]

palindromes = [content[j] for j in range(len(content)) if fwd[j] == bwd[j]]
{x : palindromes.count(x) for x in palindromes}