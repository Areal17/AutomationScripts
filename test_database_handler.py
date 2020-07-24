import unittest
from private_module.database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):

    def test_combine_string(self):
        db_handler = DatabaseHandler()
        input = ["Alpha","Beta","Gamma"]
        expected = "Alpha, Beta, Gamma"
        result = db_handler.combined_elements(input)
        self.assertEquals(result,expected, "It works")

    
if __name__ == "__main__":
    unittest.main()