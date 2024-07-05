import hashlib as hl

def generate_hashed_ids(to_hash):
    to_hash_encode = str(to_hash).encode("UTF-8")
    this_id = hl.shake_256(to_hash_encode).hexdigest(12)
    return this_id

def hash_ids_list(dataset):
    list_of_ids = []
    for row in dataset:
        unique_to_hash = row[0] + row[3]
        hashed_uid = generate_hashed_ids(unique_to_hash)
        list_of_ids.append(hashed_uid)
    return list_of_ids

