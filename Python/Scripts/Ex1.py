#!/usr/bin/env python3

# Exercise Sheet 1

# 1 Calculator

import sys

# Operator
op = {"+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "*": lambda x, y: x * y,
      "/": lambda x, y: x / y,
      "**": lambda x, y: x ** y}

if (int(sys.argv[2]) == 0 and sys.argv[3] == "/"):
    print("Error, no division by zero!") 
else:
    print(f"{sys.argv[1]} {sys.argv[3]} {sys.argv[2]} = {op[sys.argv[3]](int(sys.argv[1]), int(sys.argv[2]))}")

# 2 Symbol Counter

# 3 Sieve of Eratosthenes

def sieve(n):
    numbers = [i for i in range(2, n + 1)]
    primes = []

    while len(numbers) != 0:
        primes.append(numbers[0])
        numbers = [numbers[j] for j in range(len(numbers)) if [i % numbers[0] != 0 for i in numbers][j]]
    
    return primes

sieve(500)

sieve(sys.argv[1])