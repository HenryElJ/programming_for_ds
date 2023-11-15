#!/usr/bin/env python3

import sys
import re
import os

# Exercise Sheet 4

# 1. Parse function

def parse_csv(filename, separator, has_header):
    df = {}
    with open(filename, "r") as file_obj:
        content = file_obj.read().splitlines()
    if has_header:
        header = content[0].split(separator)
        rows = [i.split(separator) for i in content[1:]]
        for i in range(len(rows[0])):
            df[header[i]] = [row[i] for row in rows]
    else:
        rows = [i.split(separator) for i in content]
        for i in range(len(rows[0])):
            df[i] = [row[i] for row in rows]
    return df

# 2. Dictionary with Lambdas

# Already acheived this in the first exercise. No augmentation required.
# Could do opposite and look into how to do this "as intended"

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

# 3. Exceptions I

op["p"](1, 2)

def calc(input):
    # Operator
    op = {"+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "**": lambda x, y: x ** y}
    
    try: 
        return op[input[1]](input[0], input[2])
    except (KeyError) as err:
        return print("Invalid operator symbol:", err)
    except (ZeroDivisionError) as err:
        return print("Division by zero is not allowed")
    except (TypeError) as err:
        return print("Invalid operand. Both must be numeric")


# 4. Exceptions II

def calc():
    # Operator
    op = {"+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "**": lambda x, y: x ** y}
    
    form = input("Please enter formula: ")
    form = re.split("\s+", form)

    try: 
        return(op[form[1]](float(form[0]), float(form[2])))
    except (IndexError) as err:
        print("List index out of range. Add spaces between terms")
        calc()
    except (KeyError) as err:
        print("Invalid operator symbol:", err)
        print("Try again!")
        calc()
    except (ZeroDivisionError) as err:
        print("Division by zero is not allowed")
        print("Try again!")
        calc()
    except (ValueError) as err:
        print("Could not convert string to float")
        print("Try again!")
        calc()

calc()