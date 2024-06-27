from generate_menu_items import generate_menu

def test_generate_menu():
    dummy_data = {
        "Chocolate": 2.30,
        "Baked Beans": 1.95,
        "Tea": 0.80
    }
    
    expected = [
        ["P001", "Chocolate", 2.30],
        ["P002", "Baked Beans", 1.95]
        ["P003", "Tea", 0.80]
    ]