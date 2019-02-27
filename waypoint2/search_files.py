from os import walk


def scan_files(path):
    """ returns a flat list of files scanned
        recursively from the specified path """
    files_ls = []
    for dirpath, _, filenames in walk(path):
        for filename in filenames:
            files_ls.append(dirpath + '/' + filename)
    files_ls.sort()
    return files_ls