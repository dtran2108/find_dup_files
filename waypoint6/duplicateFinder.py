from waypoint5.checksumGroup import group_files_by_checksum
from waypoint3.size_group import group_files_by_size


def find_all_duplicate_files(file_path_names):
    """ returns a list of groups of duplicate files """
    sizeGrouped_files = group_files_by_size(file_path_names)
    result = []
    for group in sizeGrouped_files:
        checksumGrouped_files = group_files_by_checksum(group)
        for checksumGroup in checksumGrouped_files:
            if len(checksumGroup) > 1:
                result.append(checksumGroup)
    return result