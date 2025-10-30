#!/usr/bin/env python3
"""
Created by: Mr. Coxall
Created on: Sep 2025
This module is an example of using pandas
"""

import os
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
fred_api_key = os.getenv("FRED_API_KEY")
if not fred_api_key:
    raise EnvironmentError("FRED_API_KEY not set in .env or environment")

fred = Fred(api_key=fred_api_key)


# input
data = fred.get_series('SP500')

myvar = pd.DataFrame(data)

print(myvar)

# process
pass

# output
# Note: do not print the API key for security reasons
print("\nDone.")
