import unittest
from private_module.database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):

    def test_combine_string(self):
        db_handler = DatabaseHandler()
        input = ["Alpha","Beta","Gamma"]
        expected = "Alpha, Beta, Gamma"
        result = db_handler.combined_elements(input)
        self.assertEqual(expected,result)
        db_handler.close_connection()

    def test_get_data(self):
        db_handler = DatabaseHandler()
        input = ("SELECT Projekttitel, Kurzbezeichnung FROM VarioProjects")
        result = db_handler.select_data_from_string(input)
        print(result)
        self.assertFalse(result)


    
if __name__ == "__main__":
    unittest.main()