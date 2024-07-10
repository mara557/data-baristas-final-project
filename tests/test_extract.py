import boto3
import pytest
from moto import mock_s3
from datetime import datetime, timezone
from src.extract import reading_all_csv_files

@pytest.fixture
def s3_setup():
    """Set up the mocked S3 environment."""
    with mock_s3():
        s3 = boto3.client('s3', region_name='us-east-1')
        bucket_name = 'test-bucket'
        s3.create_bucket(Bucket=bucket_name)

        # Create mock CSV files
        today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        csv_content_1 = """25/08/2021 09:00,Testville,John Doe,"Apple - 1.2, Banana - 0.5",CARD,1234432132143214
25/08/2021 09:04,Testville,Steve Stevenson,"Hot Dog - 1.2, Half Grapefruit - 0.3",CARD,4233432232143214
25/08/2021 09:04,Testville,Bjorn Bjornnson,"Pomegranate - 2.4, Whole Grapefruit - 0.5",CASH,"""

        csv_content_2 = """05/09/2015 09:02,E World,Sam Sepiol,"Chips - 0.8, Ram Sandwich - 2.1",CASH,
05/09/2015 09:05,E World,Tyrell Wellick,"Swedish Fish - 1.15, Ketel One - 21",CARD,1234567809876543
05/09/2015 09:06,E World,Darlene Alderson,"Icing Sugar - 20, Poppies - 15",CARD,1434567409876543"""

        s3.put_object(Bucket=bucket_name, Key=f'Testville_{today}.csv', Body=csv_content_1)
        s3.put_object(Bucket=bucket_name, Key=f'EWorld_{today}.csv', Body=csv_content_2)

        yield s3, bucket_name

def test_reading_all_csv_files(s3_setup):
    """Test reading_all_csv_files function with mocked S3 environment"""
    s3, bucket_name = s3_setup
    result = reading_all_csv_files(bucket_name)

    expected_result = {
        'Testville': [
            ["25/08/2021 09:00", "Testville", "John Doe", "Apple - 1.2, Banana - 0.5", "CARD", "1234432132143214"],
            ["25/08/2021 09:04", "Testville", "Steve Stevenson", "Hot Dog - 1.2, Half Grapefruit - 0.3", "CARD", "4233432232143214"],
            ["25/08/2021 09:04", "Testville", "Bjorn Bjornnson", "Pomegranate - 2.4, Whole Grapefruit - 0.5", "CASH", ""]
        ],
        'EWorld': [
            ["05/09/2015 09:02", "E World", "Sam Sepiol", "Chips - 0.8, Ram Sandwich - 2.1", "CASH", ""],
            ["05/09/2015 09:05", "E World", "Tyrell Wellick", "Swedish Fish - 1.15, Ketel One - 21", "CARD", "1234567809876543"],
            ["05/09/2015 09:06", "E World", "Darlene Alderson", "Icing Sugar - 20, Poppies - 15", "CARD", "1434567409876543"]
        ]
    }

    # Only today's files should be processed
    today_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    for location in expected_result:
        if location not in result:
            expected_result[location] = []

    assert result == expected_result
