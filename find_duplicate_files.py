from waypoint1.parser import do_argparse
from waypoint2.search_files import scan_files
from waypoint6.duplicateFinder import find_all_duplicate_files
from waypoint7.json_convert import json_convert


def main():
    root_path = do_argparse()
    file_path_names = scan_files(root_path)
    result = find_all_duplicate_files(file_path_names)
    print(json_convert(result))


if __name__ == '__main__':
    main()
