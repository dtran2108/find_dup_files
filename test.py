from unittest import TestCase, main
from waypoint2.search_files import scan_files
from waypoint3.size_group import *
from os.path import getsize


class TestSearchFilesMethod(TestCase):

    def test_scan_files(self):
        """ check if the scan files function return
            a list of all the files from the root """
        root = '/home/dtran00/github_f/test'
        result = ['/home/dtran00/github_f/test/1',
                  '/home/dtran00/github_f/test/2',
                  '/home/dtran00/github_f/test/3',
                  '/home/dtran00/github_f/test/4',
                  '/home/dtran00/github_f/test/test1/ha',
                  '/home/dtran00/github_f/test/test1/he',
                  '/home/dtran00/github_f/test/test1/hi']
        self.assertEqual(scan_files(root), result)
    
    def test_remove_empty_files(self):
        """ check if the remove empty files function return
            a list with empty files omitted """
        ls = ['/home/dtran00/github_f/test/1',
              '/home/dtran00/github_f/test/2',
              '/home/dtran00/github_f/test/3',
              '/home/dtran00/github_f/test/4',
              '/home/dtran00/github_f/test/test1/ha',
              '/home/dtran00/github_f/test/test1/he',
              '/home/dtran00/github_f/test/test1/hi']
        result = ['/home/dtran00/github_f/test/1',
                  '/home/dtran00/github_f/test/2',
                  '/home/dtran00/github_f/test/3',
                  '/home/dtran00/github_f/test/test1/ha',
                  '/home/dtran00/github_f/test/test1/hi']
        self.assertEqual(remove_empty_files(ls), result)

    def test_get_file_size(self):
        """ check if the get file size function return a list 
            contains tuples of the file and its size in the size order """
        self.assertEqual(get_files_size(
                            ['/home/dtran00/github_f/test/1',
                             '/home/dtran00/github_f/test/2']),
                            [('/home/dtran00/github_f/test/1', 
                              getsize('/home/dtran00/github_f/test/1')),
                             ('/home/dtran00/github_f/test/2', 
                              getsize('/home/dtran00/github_f/test/2'))])




if __name__ == '__main__':
    main()