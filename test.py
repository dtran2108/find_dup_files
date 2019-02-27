from unittest import TestCase, main
from waypoint2.search_files import scan_files
from waypoint3.size_group import *
from waypoint4.getChecksum import *
from waypoint5.checksumGroup import *
from waypoint6.duplicateFinder import *
from waypoint7.json_convert import *
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
        file_ls = ['/home/dtran00/github_f/test/1',
                   '/home/dtran00/github_f/test/2']
        result = [('/home/dtran00/github_f/test/1',
                  getsize('/home/dtran00/github_f/test/1')),
                  ('/home/dtran00/github_f/test/2', 
                  getsize('/home/dtran00/github_f/test/2'))]
        self.assertEqual(get_files_size(file_ls), result)

    def test_group_files_by_size(self):
        """ check if the group files by size function return
            a list of groups of at least two files that have the same size"""
        file_ls = ['/home/dtran00/github_f/test/1',
                  '/home/dtran00/github_f/test/2',
                  '/home/dtran00/github_f/test/3',
                  '/home/dtran00/github_f/test/test1/ha',
                  '/home/dtran00/github_f/test/test1/hi']
        result = [['/home/dtran00/github_f/test/1',
                  '/home/dtran00/github_f/test/2',
                  '/home/dtran00/github_f/test/3',
                  '/home/dtran00/github_f/test/test1/ha',
                  '/home/dtran00/github_f/test/test1/hi']]
        self.assertEqual(group_files_by_size(file_ls), result)

    def test_get_files_hash(self):
        """ check if the get files hash function return
            a list with each element is a tuple
            of a file and its hash value in hash order """
        file_ls = ['/home/dtran00/github_f/test/1',
                  '/home/dtran00/github_f/test/2',
                  '/home/dtran00/github_f/test/3',
                  '/home/dtran00/github_f/test/test1/ha',
                  '/home/dtran00/github_f/test/test1/hi']
        result = [('/home/dtran00/github_f/test/2', 'e10adc3949ba59abbe56e057f20f883e'),
                  ('/home/dtran00/github_f/test/3', 'e10adc3949ba59abbe56e057f20f883e'),
                  ('/home/dtran00/github_f/test/test1/hi', 'e10adc3949ba59abbe56e057f20f883e'),
                  ('/home/dtran00/github_f/test/1', 'e80b5017098950fc58aad83c8c14978e'),
                  ('/home/dtran00/github_f/test/test1/ha', 'e80b5017098950fc58aad83c8c14978e')]
        self.assertEqual(get_files_hash(file_ls), result)

    def test_get_file_checksum(self):
        """ check if the get file checksum function
            return a md5 hash value for a file according to its path """
        file_path = '/home/dtran00/github_f/test/2'
        result = 'e10adc3949ba59abbe56e057f20f883e'
        self.assertEqual(get_file_checksum(file_path), result)

    def test_group_files_by_checksum(self):
        """ check if the group files by checksum 
            returns a list of groups of at least two
            files that have the same checksum """
        file_ls = ['/home/dtran00/github_f/test/1',
                  '/home/dtran00/github_f/test/2',
                  '/home/dtran00/github_f/test/3',
                  '/home/dtran00/github_f/test/test1/ha',
                  '/home/dtran00/github_f/test/test1/hi']
        result = [['/home/dtran00/github_f/test/2',
                   '/home/dtran00/github_f/test/3',
                   '/home/dtran00/github_f/test/test1/hi'],
                   ['/home/dtran00/github_f/test/1',
                    '/home/dtran00/github_f/test/test1/ha']]
        self.assertEqual(group_files_by_checksum(file_ls), result)

    def test_find_all_duplicate_files(self):
        """ check if the find all duplicate files
            returns a list of groups of duplicate files """
        file_ls = ['/home/dtran00/github_f/test/1',
                  '/home/dtran00/github_f/test/2',
                  '/home/dtran00/github_f/test/3',
                  '/home/dtran00/github_f/test/test1/ha',
                  '/home/dtran00/github_f/test/test1/hi']
        result = [['/home/dtran00/github_f/test/2',
                   '/home/dtran00/github_f/test/3',
                   '/home/dtran00/github_f/test/test1/hi'],
                   ['/home/dtran00/github_f/test/1',
                    '/home/dtran00/github_f/test/test1/ha']]
        self.assertEqual(find_all_duplicate_files(file_ls), result)


if __name__ == '__main__':
    main()
