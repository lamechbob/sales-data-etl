import psycopg2
import os
from dotenv import load_dotenv

# ----------------------------------------------------------
# Script: create_database.py
# Purpose:
# - Connect to an existing PostgreSQL RDS instance
# - Create a new database named `salesetl`
# Requirements:
# - Target database instance must already exist and be reachable
# - The user must have permission to create new databases
# ----------------------------------------------------------

# Step 1: Load environment variables from a .env file
# This avoids hardcoding sensitive credentials into your code
load_dotenv()

# Step 2: Retrieve DB connection parameters from environment
DB_HOST = os.getenv("DB_HOST")  # e.g. your RDS endpoint
DB_NAME = os.getenv("DB_NAME")  # this should be the *admin* database, like 'postgres'
DB_USER = os.getenv("DB_USER")  # user with CREATE DATABASE privileges
DB_PASS = os.getenv("DB_PASS")

# Step 3: Establish a connection to the PostgreSQL instance
# NOTE: Connect to an existing DB (like 'postgres'), not the one you're trying to create
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)

# Step 4: Enable autocommit mode
# CREATE DATABASE cannot run inside a transaction block, so this is required
conn.autocommit = True

# Step 5: Create a cursor and issue the CREATE DATABASE command
cur = conn.cursor()
cur.execute("CREATE DATABASE salesetl;")
print("Database 'salesetl' created successfully.")

# Step 6: Clean up
cur.close()
conn.close()
