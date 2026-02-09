#!/usr/bin/env python
import json
import os
import sys
from datetime import datetime

import fitbit
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("FITBIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("FITBIT_CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("FITBIT_ACCESS_TOKEN")
REFRESH_TOKEN = os.getenv("FITBIT_REFRESH_TOKEN")

client = fitbit.Fitbit(
    CLIENT_ID,
    CLIENT_SECRET,
    access_token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN,
)

if len(sys.argv) > 1:
    try:
        base_date = datetime.strptime(sys.argv[1], "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)
else:
    base_date = datetime.now()

try:
    entries = client.get_bodyweight(base_date=base_date, period="7d")
    print(json.dumps(entries))
except fitbit.exceptions.HTTPUnauthorized:
    print(
        "Unauthorized access. Please run ./gather_keys_oauth2.py to get access to tokens."
    )
except Exception as e:
    print(f"Error: {e}")
