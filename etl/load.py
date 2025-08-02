# etl/load.py

import boto3

def loadToS3(file_path_to_upload, bucket_to_upload_to, file_name_to_upload):

    """
    Uploads a local file to an AWS S3 bucket.

    Args:
        file_path_to_upload (str): Local path to the file (e.g., 'data/sales_data.csv')
        bucket_to_upload_to (str): Name of the S3 bucket (e.g., 'sales-etl-data-engin')
        file_name_to_upload (str): Desired name for the file in S3 (e.g., 'sales_data.csv')
    """

    print(f'\n-- Uploading "{file_name_to_upload}" to bucket "{bucket_to_upload_to}"')

    # Initialize the S3 client
    s3 = boto3.client('s3')

    try:
        # Attempt to upload the file
        s3.upload_file(file_path_to_upload, bucket_to_upload_to, file_name_to_upload)
        print('File uploaded successfully.')
    except Exception as e:
        # Catch and log any errors that occur
        print('File not uploaded. Error:', str(e))
