#!/usr/bin/env python3
import unittest
from countFiles import get_files
from countFiles import remove_hidden_files
from countFiles import get_rows_in_csv

class TestCountFile(unittest.TestCase):

    def test_countfiles_base(self):
        filePath = '/Users/ingowie/scripts'
        expected = 11
        self.assertEqual(len(get_files(filePath)), expected)
    
    def test_remove_file(self):
        test_files = [".DS_Store", "copyFiles.sh"]
        expected = ["copyFiles.sh"]
        self.assertEqual(remove_hidden_files(test_files), expected)

    def test_rows_in_csv(self):
        test_path = '/Users/ingowie/scripts/db/images.csv'
        expected = 0
        self.assertEqual(len(get_rows_in_csv(test_path)), expected)




if __name__ == "__main__":
    unittest.main()