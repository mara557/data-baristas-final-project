import boto3
import csv
import io
from datetime import datetime, timezone

s3 = boto3.client('s3')

def reading_all_csv_files(bucket, prefix=""):
    """Reads all CSV files from the specified S3 bucket and groups them by location, appending data from files with the same location."""
    all_files_data = {}
    today = datetime.now(timezone.utc).date()

    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith('.csv'):
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
                else:
                    print(f"Skipping file {key} as it was not uploaded today.")
            except Exception as e:
                print(f"Error processing file {key}: {str(e)}")
    
    return all_files_data