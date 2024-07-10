import src.generate_uids as gu

def test_hash_ids_list():
    mock_dataset = [
            ["25/08/2021 09:00", "Testville", "Apple - 1.2, Banana - 0.5", "1.7", "CARD"],
            ["25/08/2021 09:04", "Testville", "Hot Dog - 1.2, Half Grapefruit - 0.3", "1.5", "CARD"],
            ["25/08/2021 09:04", "Testville", "Pomegranate - 2.4, Whole Grapefruit - 0.5", "2.9", "CASH"],
            ["05/09/2015 09:02", "E World", "Chips - 0.8, Ram Sandwich - 2.1", "2.9", "CASH"],
            ["05/09/2015 09:05", "E World", "Swedish Fish - 1.15, Ketel One - 21", "22.15", "CARD"],
            ["05/09/2015 09:06", "E World", "Icing Sugar - 20, Poppies - 15", "35", "CARD"]
        ]
    expected = ['301f9268be7a137d802db868', 
                'f4b3673a6adcac011f05093f', 
                'f7c8b8cfdb0e69108c2f4f7c', 
                '4abaaf170ea2c3d3c6d196dc', 
                'b5b11e1b01669afe9d0e444d', 
                'f0f738c6a075774d0b7ec9df'
                ]
    result = gu.hash_ids_list(mock_dataset)
    print(result)
    assert result == expected