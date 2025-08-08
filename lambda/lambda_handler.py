import boto3
import pandas as pd
import pg8000
import os
import io
from etl import transform

# Initialize the S3 client
s3 = boto3.client('s3')


def lambda_handler(event, context):
    print("Lambda triggered.")

    # Step 1: Extract bucket and object key (file name) from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    print(f"-- S3 Bucket: {bucket_name}")
    print(f"-- S3 Object Key: {object_key}")

    incoming_file = f's3://{bucket_name}/{object_key}'
    print(f"-- Full file path: {incoming_file}")

    # Step 2: Download the file contents from S3
    print("-- Downloading file from S3")
    response = s3.get_object(Bucket=bucket_name, Key=object_key)

    print("-- Reading file body into memory")
    contents = response['Body'].read()

    # Step 3: Convert the file contents into a pandas DataFrame
    print("-- Creating DataFrame from CSV")
    lambda_df = pd.read_csv(io.BytesIO(contents), dtype=str)
    print(lambda_df)

    # Step 4: Retrieve environment variables for database connection
    print("-- Loading environment variables for database connection")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")

    try:
        # Step 5: Establish a connection to the PostgreSQL database
        print("-- Attempting to connect to PostgreSQL database")
        conn = pg8000.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        print("-- Connection to database successful")

        # Step 6: Test the connection by executing a version query
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print("-- PostgreSQL version:", version)

        # Step 7: Create table using ETL module
        print("-- Creating table in database")
        transform.createDatabasePro(conn)

        # Step 8: Insert data into table
        print("-- Inserting data into table")
        transform.updateTablePro(conn, lambda_df)

        # Step 9: Finalize database operations
        cur.close()
        conn.commit()
        conn.close()
        print("-- Database operations completed successfully")

    except Exception as e:
        # Log any errors that occur during the connection or execution
        print("Connection or execution failed:", str(e))
