import os


for dirpath, dirnames, filenames in os.walk('/home/dtran00/dup_file_finder/'):
    print('dirpath: ', os.path.abspath(dirpath))
    print('dirnames: ', dirnames)
    print('filenames: ', filenames)
    print('----------------------------')