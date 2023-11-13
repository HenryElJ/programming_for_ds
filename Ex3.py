#!/usr/bin/env python3

import sys
import re
import os

# Exercise Sheet 3

# Comprehensions I

with open("Desktop/MSc. Data Science/WS 23 24/Programming for Data Science/phone_book.csv", "r") as file_obj:
    content = file_obj.read().splitlines() 

header = content[0].split(",")
rows = [i.split(",") for i in content[1:]]

phonebook_dict = {}
for i in range(len(header)):
    phonebook_dict[header[i]] = [row[i] for row in rows]

phonebook_dict["TITLE_CLEANED"] = list(map(lambda x : re.sub("[^a-z ]", "", x.lower()), phonebook_dict["TITLE"]))
set(phonebook_dict["TITLE_CLEANED"])
# Female Inferred Titles
fem_title = ['ms', 'mrs', 'miss']
# Male Inferred Titles
male_title = ['mr', 'sr']

phonebook_dict.values()

set([phonebook_dict["FORENAME"][x] for x in range(len(phonebook_dict["TITLE_CLEANED"])) if phonebook_dict["TITLE_CLEANED"][x] in fem_title])
set([phonebook_dict["FORENAME"][x] for x in range(len(phonebook_dict["TITLE_CLEANED"])) if phonebook_dict["TITLE_CLEANED"][x] in male_title])

# Could look to clean names also

# Dictionary is annoying for this. List of Lists would have been better
[rows[x] for x in range(len(phonebook_dict["FORENAME"])) if len(phonebook_dict["FORENAME"][x]) > 8 and len(phonebook_dict["SURNAME"][x]) > 8]

set([phonebook_dict["SURNAME"][x] for x in range(len(phonebook_dict["SURNAME"])) 
     if len(re.sub("[^aeiou]", "", phonebook_dict["SURNAME"][x].lower())) > len(re.sub("[aeiou]", "", re.sub("[^a-z]", "", phonebook_dict["SURNAME"][x].lower())))])


index = sorted(range(len(phonebook_dict["SURNAME"])), key = lambda x: phonebook_dict["SURNAME"][x])

[(phonebook_dict["FORENAME"][indices], phonebook_dict["SURNAME"][indices], phonebook_dict["TITLE"][indices]) for indices in index]


# How to do in list commprehension??
rank = sorted(range(len(phonebook_dict["SURNAME"])), key = lambda x: (phonebook_dict["SURNAME"][x], phonebook_dict["FORENAME"][x]))
rank

[(phonebook_dict["SURNAME"][x], phonebook_dict["FORENAME"][x]) for x in rank]

# 2. Comprehensions II

A = [1,2,3,4]
B = [1,3,5]

[[a ** b for b in B] for a in A]

# 3. Sets

set(phonebook_dict["SURNAME"]) & set(phonebook_dict["FORENAME"])
set(phonebook_dict["SURNAME"]) | set(phonebook_dict["FORENAME"])
set(phonebook_dict["SURNAME"]) ^ set(phonebook_dict["FORENAME"])
(set(phonebook_dict["SURNAME"]) | set(phonebook_dict["FORENAME"])) - (set(phonebook_dict["SURNAME"]) & set(phonebook_dict["FORENAME"]))
set(phonebook_dict["SURNAME"]) - set(phonebook_dict["FORENAME"])
