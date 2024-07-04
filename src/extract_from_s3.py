import csv
import io
import boto3

def lambda_handler(event, context):
    """Lambda function to read all CSV files from a specified S3 bucket"""
    
    # Get bucket name and prefix from the event, or use default values
    bucket_name = event.get('bucket_name', 'your-default-bucket-name')
    prefix = event.get('prefix', '')
    
    all_files_data = {}
    
    # Create an S3 client
    s3 = boto3.client('s3')
    
    # List objects in the bucket with the given prefix
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    # Iterate through each object
    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith('.csv'):
            try:
                # Get the object from S3
                response = s3.get_object(Bucket=bucket_name, Key=key)
                
                # Read the content of the file
                content = response['Body'].read().decode('utf-8')
                
                # Parse CSV content
                csv_file = csv.reader(io.StringIO(content))
                all_files_data[key] = list(csv_file)
            except Exception as e:
                print(f"Error reading file {key}: {str(e)}")
    
    return {
        'statusCode': 200,
        'body': f"Processed {len(all_files_data)} CSV files from {bucket_name}"
    }