#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("ATTACKIQ_PLATFORM_URL")
token = os.getenv("ATTACKIQ_API_TOKEN")
assessment_id = os.getenv("ASSESSMENT_ID")

if not url or not token:
    print("Missing ATTACKIQ_PLATFORM_URL or ATTACKIQ_API_TOKEN")
    sys.exit(1)

if not assessment_id:
    print("Missing ASSESSMENT_ID")
    sys.exit(1)

from aiq_platform_api import AttackIQRestClient
from aiq_platform_api.assessment_use_cases import get_recent_run_id, get_last_run_details

client = AttackIQRestClient(url, token)

run_id = get_recent_run_id(client, assessment_id)
print(f"Run ID: {run_id}")

details = get_last_run_details(client, assessment_id)
if details:
    print("\nRun Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")