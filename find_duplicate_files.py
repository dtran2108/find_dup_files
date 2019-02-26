from argparse import ArgumentParser
from os import walk
from os.path import getsize
from itertools import groupby
from hashlib import md5


def do_argparse():
    """ do the argparse and return the path argument """
    parser = ArgumentParser()
    parser.add_argument('--path', help='The root directory to'
                        ' start scanning for duplicate files.')
    args = parser.parse_args()
    path = args.path
    return path


def scan_files(path):
    """ returns a flat list of files scanned
        recursively from the specified path """
    files_ls = []
    for dirpath, _, filenames in walk(path):
        for filename in filenames:
            files_ls.append(dirpath + '/' + filename)
    return files_ls


def remove_empty_files(file_list):
    """ return a list of files path without empty files"""
    temp = [file_name for file_name in file_list
            if getsize(file_name) == 0]
    for _file in temp:
        file_list.remove(_file)
    return file_list


def get_files_size(file_list):
    """ return a list with each element is a tuple
        of a file and its size in size order """
    result = []
    for _file in file_list:
        size = getsize(_file)
        result.append((_file, size))
    return sorted(result, key=lambda x: x[1])


def group_files_by_size(file_path_names):
    """ returns a list of groups of at least two
        files that have the same size """
    files_ls = remove_empty_files(file_path_names)
    files_ls = get_files_size(files_ls)
    groups = []
    for _, file_group in groupby(files_ls, lambda y: y[1]):
        files = [_file[0] for _file in file_group]
        groups.append(files)
    return [group for group in groups if len(group) > 1]


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


def group_files_by_checksum(file_path_names):
    """ returns a list of groups of at least two
        files that have the same checksum """
    files_ls = get_files_hash(file_path_names)
    groups = []
    for _, file_group in groupby(files_ls, lambda x: x[1]):
        files = [_file[0] for _file in file_group]
        groups.append(files)
    return [group for group in groups if len(group) > 1]


def find_all_duplicate_files(file_path_names):
    """ returns a list of groups of duplicate files """
    sizeGrouped_files = group_files_by_size(file_path_names)
    checksumGrouped_files = group_files_by_checksum(sizeGrouped_files)
    print(checksumGrouped_files)


def main():
    root_path = do_argparse()
    file_path_names = scan_files(root_path)
    grouped_files = group_files_by_size(file_path_names)
    print(grouped_files)
    print(get_file_checksum('/home/dtran00/intek_file_finder/test/1'))
    print(group_files_by_checksum(['/home/dtran00/intek_file_finder/test/3', '/home/dtran00/intek_file_finder/test/test1/ha']))
    print('find all dup files: ', find_all_duplicate_files(file_path_names))


if __name__ == '__main__':
    main()
