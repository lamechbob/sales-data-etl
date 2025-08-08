import json
from lambda_handler import lambda_handler

# ----------------------------------------------------------
# Test Script: Simulates an AWS Lambda trigger locally
# Purpose:
# - Load a mock S3 event from a local JSON file
# - Pass it to the lambda_handler function
# - Allows for fast local testing of the ETL logic
# ----------------------------------------------------------

# Load a fake S3 event from a JSON file
# This file mimics the structure of an actual S3 trigger event
with open('../data/fake_event.json') as f:
    event = json.load(f)

# Invoke the Lambda function with the fake event
# The second argument (context) is set to None, which is fine for local testing
lambda_handler(event, None)

