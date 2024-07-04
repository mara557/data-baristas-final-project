import pytest
from unittest.mock import mock_open, patch

# Import the function to be tested
from src.extract import reading_all_csv_files

@pytest.fixture
def mock_csv_files():
    """Fixture to provide mock CSV file data"""
    file1_content = """25/08/2021 09:00,Testville,John Doe,"Apple - 1.2, Banana - 0.5",CARD,1234432132143214
25/08/2021 09:04,Testville,Steve Stevenson,"Hot Dog - 1.2, Half Grapefruit - 0.3",CARD,4233432232143214
25/08/2021 09:04,Testville,Bjorn Bjornnson,"Pomegranate - 2.4, Whole Grapefruit - 0.5",CASH,"""

    file2_content = """05/09/2015 09:02,E World,Sam Sepiol,"Chips - 0.8, Ram Sandwich - 2.1",CASH,
05/09/2015 09:05,E World,Tyrell Wellick,"Swedish Fish - 1.15, Ketel One - 21",CARD,1234567809876543
05/09/2015 09:06,E World,Darlene Alderson,"Icing Sugar - 20, Poppies - 15",CARD,1434567409876543"""

    return {
        "data/file1.csv": file1_content,
        "data/file2.csv": file2_content
    }

def test_reading_all_csv_files(mock_csv_files):
    """Test reading_all_csv_files function with mocked CSV files"""
    directory = "data"
    expected_result = {
        f"file1.csv": [
            ["25/08/2021 09:00", "Testville", "John Doe", "Apple - 1.2, Banana - 0.5", "CARD", "1234432132143214"],
            ["25/08/2021 09:04", "Testville", "Steve Stevenson", "Hot Dog - 1.2, Half Grapefruit - 0.3", "CARD", "4233432232143214"],
            ["25/08/2021 09:04", "Testville", "Bjorn Bjornnson", "Pomegranate - 2.4, Whole Grapefruit - 0.5", "CASH", ""]
        ],
        f"file2.csv": [
            ["05/09/2015 09:02", "E World", "Sam Sepiol", "Chips - 0.8, Ram Sandwich - 2.1", "CASH", ""],
            ["05/09/2015 09:05", "E World", "Tyrell Wellick", "Swedish Fish - 1.15, Ketel One - 21", "CARD", "1234567809876543"],
            ["05/09/2015 09:06", "E World", "Darlene Alderson", "Icing Sugar - 20, Poppies - 15", "CARD", "1434567409876543"]
        ]
    }

    mock_glob = lambda pattern: list(mock_csv_files.keys())

    # Create a dictionary to map file paths to their content
    file_contents = {
        "data/file1.csv": mock_csv_files["data/file1.csv"],
        "data/file2.csv": mock_csv_files["data/file2.csv"],
    }

    def mocked_open(file, mode='r', encoding="UTF-8", newline=None):
        # Return the correct mock content based on the file path
        if file in file_contents:
            return mock_open(read_data=file_contents[file]).return_value
        return mock_open().return_value

    with patch("glob.glob", mock_glob):
        with patch("builtins.open", new=mocked_open):
            result = reading_all_csv_files(directory)
            assert result == expected_result
