#!/usr/bin/env python3

# Exercise Sheet 8

# 1. NumPy masking

import numpy as np
import pandas as pd

years = np.random.randint(0, 5000, 100)

leap_years = years[[i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) for i in years]]

len(leap_years)
min(leap_years); max(leap_years)
np.sort(leap_years)[::-1]

# 2. Pandas basics

dummy_data = [{"first_name" : "Joe",     "last_name" : "Johnson",   "phone" : "123", "zip_code" : 12055, "age" : 26, "height" : 178, "weight" : 72},
              {"first_name" : "Allen",   "last_name" : "White",     "phone" : "456", "zip_code" : 12059, "age" : 35, "height" : 180, "weight" : 80},
              {"first_name" : "Sarah",   "last_name" : "Michael",   "phone" : "789", "zip_code" : 10023, "age" : 47, "height" : 165, "weight" : 65},
              {"first_name" : "Kate",    "last_name" : "Tree",      "phone" : "101", "zip_code" : 23109, "age" : 55, "height" : 134, "weight" : 53}]

dummy_dataframe = pd.DataFrame(dummy_data)

dummy_dataframe[["first_name", "last_name", "age"]][dummy_dataframe["age"] < 28]
dummy_dataframe[["last_name", "first_name", "height", "age"]][(dummy_dataframe["age"] < 28) & (dummy_dataframe["height"] > 175)]
dummy_dataframe["age"] += 1
dummy_dataframe["bmi"] = dummy_dataframe["weight"] / (dummy_dataframe["height"] / 100) ** 2
dummy_dataframe[["first_name", "last_name", "zip_code"]][(dummy_dataframe["zip_code"] >= 10115) & (dummy_dataframe["zip_code"] <= 14199)]