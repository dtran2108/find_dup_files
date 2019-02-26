from waypoint4.getChecksum import get_files_hash
from itertools import groupby


def group_files_by_checksum(file_path_names):
    """ returns a list of groups of at least two
        files that have the same checksum """
    files_ls = get_files_hash(file_path_names)
    groups = []
    for _, file_group in groupby(files_ls, lambda x: x[1]):
        files = [_file[0] for _file in file_group]
        groups.append(files)
    return [group for group in groups if len(group) > 1]