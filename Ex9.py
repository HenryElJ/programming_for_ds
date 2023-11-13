#!/usr/bin/env python3

# Exercise Sheet 9

import sys
import numpy as np
import pandas as pd
import Levenshtein as lev
import matplotlib.pyplot as plt
import itertools
import time

# 1. Phone book

# 1.1 Query

df = pd.read_csv("Desktop/MSc. Data Science/phone_book.csv")
list(df)

df[["SURNAME", "FORENAME", "TITLE", "PHONE", "EMAIL"]]

# name: sys.argv[1]
# phone: sys.argv[2]
# max_error: sys.argv[3]

cond1 = [lev.distance(forename.lower(), sys.argv[1].lower()) < sys.argv[2] for forename in df["FORENAME"].fillna("")]
cond2 = [lev.distance(surname.lower(), sys.argv[1].lower()) < sys.argv[2] for surname in df["SURNAME"].fillna("")]
if sys.argv[3] == True:
    cond3 = df["PHONE"].notna().tolist()
else:
    cond3 = [True for i in range(len(df["PHONE"]))]

index = [(i == True | j == True) & k == True for i, j, k in zip(cond1, cond2, cond3)]
sum(index)

df[index].sort_values(["SURNAME", "FORENAME", "PHONE"])

# 1.2 Analysis

df = pd.read_csv("Desktop/MSc. Data Science/phone_book.csv")

df["TITLE_CLEANED"] = df["TITLE"].str.lower().replace("[^A-Za-z ]", "", regex = True)

plt.pie(df["TITLE_CLEANED"].value_counts()[:5], labels = df["TITLE_CLEANED"].value_counts()[:5].keys())
plt.show()

df["TITLE_CLEANED"] = df["TITLE_CLEANED"].replace("miss", "mrs")

plt.pie(df["TITLE_CLEANED"].value_counts()[:5], labels = df["TITLE_CLEANED"].value_counts()[:5].keys())
plt.show()

df["FORENAME_CLEANED"] = [forename.split(" ", 1)[0].lower() for forename in df["FORENAME"].fillna("")]

# to_plot = df.groupby(["TITLE_CLEANED", "FORENAME_CLEANED"]).size().reset_index(name = "FREQ").set_index("FORENAME_CLEANED").groupby("TITLE_CLEANED")["FREQ"].nlargest(5)

# outer = to_plot.reset_index(name = "FREQ").groupby("TITLE_CLEANED")["FREQ"].sum()
# inner = to_plot
# inner_labels = to_plot.index.get_level_values(1)

# fig, ax = plt.subplots(figsize=(24, 12))
# size = 0.3

# ax.pie(outer.values.flatten(), radius=1,
#        labels=outer.index,
#        autopct='%1.1f%%',
#        wedgeprops=dict(width=size, edgecolor='w'))

# ax.pie(inner.values.flatten(), radius=1-size, 
#        labels = inner_labels,
#        wedgeprops=dict(width=size, edgecolor='w'))

# ax.set(aspect="equal", title='Pie plot with `ax.pie`')
# plt.show()

to_plot = df[df["TITLE_CLEANED"].isin(df["TITLE_CLEANED"].value_counts()[:5].reset_index()["TITLE_CLEANED"])]
to_plot = to_plot.groupby(["TITLE_CLEANED", "FORENAME_CLEANED"]).size().reset_index(name = "FREQ").set_index("FORENAME_CLEANED").groupby("TITLE_CLEANED")["FREQ"].nlargest(5)

outer = to_plot.reset_index(name = "FREQ").groupby("TITLE_CLEANED")["FREQ"].sum()
inner = to_plot
inner_labels = to_plot.index.get_level_values(1)

fig, ax = plt.subplots(figsize=(24, 12))
size = 0.3

ax.pie(outer.values.flatten(), radius = 1,
       labels = outer.index,
       # autopct='%1.1f%%',
       explode = list(itertools.repeat(0.05, len(outer.index))),
       wedgeprops = dict(width = size, edgecolor = 'w'))

ax.pie(inner.values.flatten(), radius = 1 - size, 
       labels = inner_labels,
       wedgeprops = dict(width = size, edgecolor = 'w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()

df.groupby(["TITLE_CLEANED"])["SURNAME"].apply(lambda x : np.mean(x.str.len()))

# 1.3 Phone Sharing

df = pd.read_csv("Desktop/MSc. Data Science/phone_book.csv")

df.apply()

start = time.perf_counter()
df[df["PHONE"].isin([x for x in df["PHONE"] if df["PHONE"].tolist().count(x) > 1 and pd.notnull(x)])][["PHONE", "TITLE", "FORENAME", "SURNAME"]].sort_values("PHONE")
end = time.perf_counter()
print(round(end - start, 3))
# [x for x in df["PHONE"] if df["PHONE"].tolist().count(x) > 1 and pd.notnull(x)]