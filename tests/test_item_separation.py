def mock_item_separation():
    # Mock data simulating the read CSV data
    all_files_data = {
        "file1.csv": [
            ["25/08/2021 09:00", "Testville", "John Doe", "Apple - 1.2, Banana - 0.5", "1.7", "CARD", "1234432132143214"],
            ["25/08/2021 09:04", "Testville", "Steve Stevenson", "Hot Dog - 1.2, Half Grapefruit - 0.3", "1.5", "CARD", "4233432232143214"],
            ["25/08/2021 09:04", "Testville", "Bjorn Bjornnson", "Pomegranate - 2.4, Whole Grapefruit - 0.5", "2.9", "CASH",]
        ],
        "file2.csv": [
            ["05/09/2015 09:02", "E World", "Sam Sepiol", "Chips - 0.8, Ram Sandwich - 2.1", "2.9", "CASH",],
            ["05/09/2015 09:05", "E World", "Tyrell Wellick", "Swedish Fish - 1.15, Ketel One - 21", "22.15", "CARD", "1234567809876543"],
            ["05/09/2015 09:06", "E World", "Darlene Alderson", "Icing Sugar - 20, Poppies - 15", "35", "CARD", "1434567409876543"]
        ]
    }
    
    # Mock function to remove PII (personally identifiable information)
    def mock_remove_pii(data):
        cleaned_data = []
        for row in data:
            cleaned_row = row[:2] + row[3:4]
            cleaned_data.append(cleaned_row)
        return cleaned_data

    # Mock function to hash order IDs
    def mock_hash_ids_list(dataset):
        return [f"order_{i+1}" for i in range(len(dataset))]

    all_results = {}
    for filepath, data in all_files_data.items():
        file_name = filepath.split('/')[-1]
        all_data = mock_remove_pii(data)
        
        dataset = []
        for row in all_data:
            if len(row) > 2:  # Ensure the row has the items column
                dataset.append(row)

        ids_list = mock_hash_ids_list(dataset)

        result = []
        for order_index, row in zip(ids_list, dataset):
            items = row[2].split(", ")
            for item in items:
                name, price = item.rsplit(" - ", 1)
                result.append([order_index, name.strip(), float(price.strip())])

        all_results[file_name] = result

    return all_results

def test_mock_item_separation():
    expected_result = {
        "file1.csv": [
            ["order_1", "Apple", 1.2],
            ["order_1", "Banana", 0.5],
            ["order_2", "Hot Dog", 1.2],
            ["order_2", "Half Grapefruit", 0.3],
            ["order_3", "Pomegranate", 2.4],
            ["order_3", "Whole Grapefruit", 0.5]
        ],
        "file2.csv": [
            ["order_1", "Chips", 0.8],
            ["order_1", "Ram Sandwich", 2.1],
            ["order_2", "Swedish Fish", 1.15],
            ["order_2", "Ketel One", 21.0],
            ["order_3", "Icing Sugar", 20.0],
            ["order_3", "Poppies", 15.0]
        ]
    }
    result = mock_item_separation()
    assert result == expected_result