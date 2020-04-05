import os
import hashlib
from collections import defaultdict


def block_reader(file_object, block_size=1024):
    """
    Read file in blocks of 1024 bytes
    Params:
    file_object : file
    block_size : int (default 1024 bytes)
    """
    while True:
        file_block = file_object.read(block_size)
        if not file_block:
            return
        yield file_block


def generate_hash(filename, single_block=False, hash=hashlib.sha1):
    """
    Generates hash_digest for a given file, returns hexdigest
    Params:
    filename : str (fully qualified filename)
    single_block : boolean (generate hash as single block, default False)
    hash : hashlib (hashing algo type, default sha1)
    """
    hash_object = hash()
    file_object = open(filename, 'rb')

    if single_block:
        hash_object.update(file_object.read(1024))
    else:
        for file_block in block_reader(file_object):
            hash_object.update(file_block)
    hash_digest = hash_object.hexdigest()
    file_object.close()
    return hash_digest


def find_duplicates(base_dir=os.getcwd()):
    """
    find duplicate files in given directory, returns multi valued dict of duplicate files
    Params:
    base_dir : str (fully qualified directory path, default path is current execution directory)
    """
    size_hash_dict = {}
    block_hash_dict = {}
    duplicate_hash_dict = defaultdict(set)

    for file in os.listdir(base_dir):

        full_path = os.path.join(base_dir, file)
        try:
            # if given link is softlink (symlink), override it with actual path
            full_path = os.path.realpath(full_path)
            file_size = os.path.getsize(full_path)
        except (OSError,):
            print("ERROR: File not accessible - skipping file %s", file)
            continue

        duplicate_file = size_hash_dict.get(file_size)

        if duplicate_file:
            size_hash_dict[file_size].append(full_path)
        else:
            size_hash_dict[file_size] = []  # create the list for this file size
            size_hash_dict[file_size].append(full_path)

    # For files with the same size, get their hash on the 1st block (block_size=1024 bytes)
    for __, files in size_hash_dict.items():
        if len(files) < 2:
            continue  # skipping unique files if size is different

        for file in files:
            try:
                small_hash = generate_hash(file, True)
            except (OSError,):
                # For large files, there is a possibility that file access might've changed till the exec point got here
                print("ERROR: File not accessible - skipping file %s", file)
                continue

            duplicate_file = block_hash_dict.get(small_hash)
            if duplicate_file:
                block_hash_dict[small_hash].append(file)
            else:
                block_hash_dict[small_hash] = []
                block_hash_dict[small_hash].append(file)

    # For all files with the hash on the 1st 1024 bytes, get their hash on the full file - collisions will be duplicates
    for __, files in block_hash_dict.items():

        if len(files) < 2:
            continue  # this hash of fist file block is unique, hence skipping the comparison

        for file in files:
            try:
                full_hash = generate_hash(file)
            except (OSError,):
                # For large files, there is a possibility that file access might've changed till the exec point got here
                print("ERROR: File not accessible - skipping file %s", file)
                continue

            duplicate_file = duplicate_hash_dict.get(full_hash)
            if duplicate_file:
                duplicate_hash_dict[full_hash].add(file)
            else:
                duplicate_hash_dict[full_hash].add(file)
    return duplicate_hash_dict


def print_duplicates(duplicates_dict):
    for values in duplicates_dict.values():
        print(', '.join(values))


if __name__ == "__main__":
    duplicates = find_duplicates()
    print_duplicates(duplicates)
