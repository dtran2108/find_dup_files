import argparse
import os


def do_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='The root directory to'
                        ' start scanning for duplicate files.')
    args = parser.parse_args()
    path = args.path
    return path


def scan_files(path):
    """ returns a flat list of files scanned
        recursively from the specified path """
    files_ls = []
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            files_ls.append(dirpath + '/' + filename)
    return files_ls


def remove_empty_files(file_list):
    """ return a list of files path without empty files"""
    temp = [file_name for file_name in file_list 
            if os.path.getsize(file_name) == 0]
    for _file in temp:
        file_list.remove(_file)
    return file_list


def group_files_by_size(file_path_names):
    """ returns a list of groups of at least two 
        files that have the same size """
    files_ls = remove_empty_files(file_path_names)
    groups = []
    return groups


def main():
    root_path = do_argparse()
    file_path_names = scan_files(root_path)
    group_files_by_size(file_path_names)


if __name__ == '__main__':
    main()