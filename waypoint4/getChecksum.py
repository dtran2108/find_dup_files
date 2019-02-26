from hashlib import md5


def get_files_hash(file_list):
    """ return a list with each element is a tuple
        of a file and its hash value in hash order """
    result = []
    for _file in file_list:
        hash_value = get_file_checksum(_file)
        result.append((_file, hash_value))
    return sorted(result, key=lambda x: x[1])


def get_file_checksum(file_path):
    """ return a md5 hash value for a file according to its path """
    with open(file_path) as f:
        content = f.read()
    return md5(content.encode()).hexdigest()