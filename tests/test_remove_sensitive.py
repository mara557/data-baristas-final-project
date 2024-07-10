import src.remove_sensitive as rs

def test_remove_sensitive():
    
    mock_dataset = [
        ["25/08/2021 09:00", "Testville", "John Doe", "Apple - 1.2, Banana - 0.5", "1.7", "CARD", "1234432132143214"],
        ["25/08/2021 09:04", "Testville", "Steve Stevenson", "Hot Dog - 1.2, Half Grapefruit - 0.3", "1.5", "CARD", "4233432232143214"],
        ["25/08/2021 09:04", "Testville", "Bjorn Bjornnson", "Pomegranate - 2.4, Whole Grapefruit - 0.5", "2.9", "CASH", ""],
        ["05/09/2015 09:02", "E World", "Sam Sepiol", "Chips - 0.8, Ram Sandwich - 2.1", "2.9", "CASH", ""],
        ["05/09/2015 09:05", "E World", "Tyrell Wellick", "Swedish Fish - 1.15, Ketel One - 21", "22.15", "CARD", "1234567809876543"],
        ["05/09/2015 09:06", "E World", "Darlene Alderson", "Icing Sugar - 20, Poppies - 15", "35", "CARD", "1434567409876543"]
    ]
    expected = [
        ["25/08/2021 09:00", "Testville", "Apple - 1.2, Banana - 0.5", "1.7", "CARD"],
        ["25/08/2021 09:04", "Testville", "Hot Dog - 1.2, Half Grapefruit - 0.3", "1.5", "CARD"],
        ["25/08/2021 09:04", "Testville", "Pomegranate - 2.4, Whole Grapefruit - 0.5", "2.9", "CASH"],
        ["05/09/2015 09:02", "E World", "Chips - 0.8, Ram Sandwich - 2.1", "2.9", "CASH"],
        ["05/09/2015 09:05", "E World", "Swedish Fish - 1.15, Ketel One - 21", "22.15", "CARD"],
        ["05/09/2015 09:06", "E World", "Icing Sugar - 20, Poppies - 15", "35", "CARD"]
    ]
    result = rs.remove_pii(mock_dataset)
    print(result)
    assert result == expected