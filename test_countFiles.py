#!/usr/bin/env python3
import unittest
from countFiles import get_files
from countFiles import remove_hidden_files
from countFiles import get_rows_in_csv
from countFiles import number_of_new_files

class TestCountFile(unittest.TestCase):

    def test_countfiles_base(self):
        filePath = '/Users/ingowie/scripts'
        expected = 15
        self.assertEqual(len(get_files(filePath)), expected)
    
    def test_remove_file(self):
        test_files = [".DS_Store", "copyFiles.sh"]
        expected = ["copyFiles.sh"]
        self.assertEqual(remove_hidden_files(test_files), expected)

    def test_rows_in_csv(self):
        test_path = '/Users/ingowie/scripts/db/images.csv'
        expected = 0
        self.assertEqual(len(get_rows_in_csv(test_path)), expected)

    def test_number_of_new_files(self):
        #test_path = '/Users/ingowie/scripts/db/images.csv'
        expected = 1
        file_objects = get_files('/Users/ingowie/Scripts')
        self.assertEqual(number_of_new_files(file_objects,"/Users/ingowie/Scripts/db"), expected)




if __name__ == "__main__":
    unittest.main()