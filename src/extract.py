import boto3
import csv
import io
from datetime import datetime, timezone

s3 = boto3.client('s3')

PROCESSED_FILES_LOG_BUCKET = 'data-baristas-lambda-bucket'
PROCESSED_FILES_LOG_KEY = 'processed_files.log'

def get_processed_files():
    try:
        response = s3.get_object(Bucket=PROCESSED_FILES_LOG_BUCKET, Key=PROCESSED_FILES_LOG_KEY)
        processed_files = response['Body'].read().decode('utf-8').splitlines()
    except s3.exceptions.NoSuchKey:
        processed_files = []
    return processed_files

def is_file_processed(filename, processed_files):
    return filename in processed_files

def mark_file_as_processed(filename, processed_files):
    processed_files.append(filename)
    processed_files_content = "\n".join(processed_files)
    s3.put_object(Bucket=PROCESSED_FILES_LOG_BUCKET, Key=PROCESSED_FILES_LOG_KEY, Body=processed_files_content)

def reading_all_csv_files(bucket, prefix=""):
    """Reads all CSV files from the specified S3 bucket and groups them by location, appending data from files with the same location."""
    all_files_data = {}
    today = datetime.now(timezone.utc).date()

    processed_files = get_processed_files()

    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith('.csv'):
            # Check if the file has already been processed
            if is_file_processed(key, processed_files):
                print(f"Skipping already processed file: {key}")
                continue

            try:
                response = s3.get_object(Bucket=bucket, Key=key)
                file_content = response['Body'].read().decode('utf-8')
                
                # Check the LastModified date
                last_modified = obj['LastModified'].date()
                
                # Process only today's files
                if last_modified == today:
                    csv_file = csv.reader(io.StringIO(file_content))
                    data = list(csv_file)
                    
                    location = key.split('_')[0]  # Assuming the location is the first part of the filename
                    if location not in all_files_data:
                        all_files_data[location] = []
                    
                    all_files_data[location].extend(data)
                    print(f"Processed file: {key}")
                    
                    # Mark file as processed
                    mark_file_as_processed(key, processed_files)
                else:
                    print(f"Skipping file {key} as it was not uploaded today.")
            except Exception as e:
                print(f"Error processing file {key}: {str(e)}")
    
    return all_files_data