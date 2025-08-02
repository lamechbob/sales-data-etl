# upload_s3_app.py

# Import the load module from the etl package
from etl import load

# Define upload configuration
bucket_to_upload_to = 'sales-etl-data-engin'           # Target S3 bucket name
file_name_to_upload = 'sales_data.csv'                 # Desired name for the file in S3
file_path_to_upload = 'data/sales_data.csv'            # Local file path to upload

# Call the function to upload the file to S3
load.loadToS3(file_path_to_upload, bucket_to_upload_to, file_name_to_upload)
