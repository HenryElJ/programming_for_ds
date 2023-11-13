#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Exercise Sheet 7

# 1. The Border Array

i = 4
j = 5
array = np.ones((i, j))
np.pad(array, pad_width = 1)

array = np.concatenate((np.zeros((1, j)), array), axis = 0)
array = np.concatenate((array, np.zeros((1, j))), axis = 0)
array = np.concatenate((np.zeros((i + 2, 1)), array), axis = 1)
array = np.concatenate((array, np.zeros((i + 2, 1))), axis = 1)
array

# 2. The Checkerboard

n = 4
checkerboard = np.zeros((n, n))
# Odd rows, even columns
checkerboard[1::2, ::2] = 1
# Even rows, odd columns
checkerboard[::2, 1::2] = 1

# 3. Array Comparison

A = np.array([ 0, 10, 20, 40, 60])
B = np.array([ 0, 40])

np.isin(A, B)

# List comprehension is technically a loop (??)
[x in B for x in A]

# Comparison operators and aggregators
list(map(lambda x: any(x == B), A))

A[np.isin(A, B)]
np. intersect1d(A, B)

# 4. NumPy Mixed

C = np.random.rand(3, 1, 4).round(2)
C

i = 0
np.sort(C, axis = i)

C.shape
C = np.squeeze(C)
C.shape

np.zeros((5, 5)) + list(range(5))

D = np.arange(200)
np.sum(D[np.where((D % 7 == 0) | (D % 11 == 0))])

i = 0
np.stack(([1, 2, 3], [4, 5, 6]), axis = i)

E = np.random.rand(10)
x = 0.5
E[np.where(E > x)]

np.partition(E, 4)

k = 3
E[np.argpartition(E, k)]


# (optional) Use NumPy to compute a histogram for a given array using functions linspace, searchsorted, unique
F = np.random.randn(1_000_000)

bins = np.linspace(min(F), max(F), num = 100)
width = np.diff(bins, axis = 0)[0]
heights = np.searchsorted(np.sort(F), bins)
heights = np.diff(heights, axis = 0)

plt.bar(bins[:-1], 
        heights, 
        width = width)
plt.xlim(min(F), min(F))
plt.show()

# https://stackoverflow.com/questions/9141732/how-does-numpy-histogram-work
hist, bin_edges = np.histogram(F, bins = 10)
plt.bar(bin_edges[:-1], 
        hist, 
        width = 1)
plt.xlim(min(F), min(F))
plt.show()