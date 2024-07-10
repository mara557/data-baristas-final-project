from src.generate_uids import hash_ids_list

def test_hash_ids_list():
    mock_dataset = [
        ["25/08/2021 09:00", "Testville", "Apple - 1.2, Banana - 0.5", "1.7", "CARD"],
        ["25/08/2021 09:04", "Testville", "Hot Dog - 1.2, Half Grapefruit - 0.3", "1.5", "CARD"],
        ["25/08/2021 09:04", "Testville", "Pomegranate - 2.4, Whole Grapefruit - 0.5", "2.9", "CASH"],
        ["05/09/2015 09:02", "E World", "Chips - 0.8, Ram Sandwich - 2.1", "2.9", "CASH"],
        ["05/09/2015 09:05", "E World", "Swedish Fish - 1.15, Ketel One - 21", "22.15", "CARD"],
        ["05/09/2015 09:06", "E World", "Icing Sugar - 20, Poppies - 15", "35", "CARD"]
    ]

    # Calculate the expected hash values using the generate_hashed_ids function logic
    expected = [
        'bdca27dc12dfdbd7a4f33f09',
        'd7883d793b75358804876053',
        'ee89af6227745be6259a78d6',
        'f2e12fe8e9ad07b53dcf6e45',
        '828829e2bea738543b31f333',
        'aa33580d9c323a29d673a447'
    ]

    result = hash_ids_list(mock_dataset)
    print(result)
    assert result == expected
