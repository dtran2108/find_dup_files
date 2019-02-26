from os.path import getsize
from itertools import groupby


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