from src.generate_menu_items import generate_menu

def test_generate_menu():
    dummy_data = [
        {"item_name": "Chocolate", "price": 2.30},
        {"item_name": "Chocolate", "price": 2.30},
        {"item_name": "Baked Beans", "price": 1.85},
        {"item_name": "Tea", "price": 0.80}
    ]
    
    expected = [
        ["P000", "Chocolate", 2.3],
        ["P001", "Baked Beans", 1.85],
        ["P002", "Tea", 0.8]
    ]
    
    result = generate_menu(dummy_data)
    
    assert result == expected