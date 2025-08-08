import pg8000
import os
from dotenv import load_dotenv

from etl import transform  # Optional import, only needed if you're calling transform functions

# This script tests the connection to the PostgreSQL RDS instance
# It's useful for confirming your .env credentials and RDS configuration are correct

# Step 1: Load environment variables from the .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Step 2: Try to connect to the database
try:
    conn = pg8000.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

    # Step 3: Run a simple query to confirm the connection
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("Connected. PostgreSQL version:", version)

    # Step 4: Clean up
    cur.close()
    conn.close()

except Exception as e:
    print("Connection failed:", str(e))
