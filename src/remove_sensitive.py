def remove_pii(dataset):
    """Removes pii from each dataset passed in"""
    expunged_data = []
    for row in dataset:
        row.pop(2)
        row.pop(5)
        expunged_data.append(row)
    return expunged_data

