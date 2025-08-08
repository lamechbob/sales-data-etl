# upload_s3_app.py

# This script uploads a local CSV file to a specified S3 bucket.
# Uploading the file will automatically trigger the Lambda function via S3 event notifications.

# Import the load module from the etl package
from etl import load

# Define upload configuration
bucket_to_upload_to = 'sales-etl-data-engin'              # Name of the target S3 bucket
file_name_to_upload = 'sales_data.csv'                    # Destination file name in S3
file_path_to_upload = '../data/sales_data.csv'            # Local path to the CSV file

# Trigger the upload function
# This will copy the local CSV to the S3 bucket under the specified name
load.loadToS3(file_path_to_upload, bucket_to_upload_to, file_name_to_upload)
