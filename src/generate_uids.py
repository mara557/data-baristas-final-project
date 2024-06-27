import extract as ex
import hashlib as hl

def generate_hashed_ids(to_hash):
    to_hash_encode = str(to_hash).encode("UTF-8")
    this_id = hl.shake_256(to_hash_encode).hexdigest(7)
    return this_id

def hash_ids_list(dataset):
    list_of_ids = []
    for row in dataset:
        unique_to_hash = row[0] + row[2]
        list_of_ids.append(generate_hashed_ids(unique_to_hash))
    return list_of_ids

# example usage below:
leeds_data = ex.reading_leeds_csv_files()
chesterfield_data = ex.reading_chesterfield_csv_files()

leeds_ids = hash_ids_list(leeds_data)
chesterfield_ids = hash_ids_list(chesterfield_data)

