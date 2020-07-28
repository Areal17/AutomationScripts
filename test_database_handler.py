#!/usr/bin/env python3
import unittest
from private_module.database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    
    def setUp(self):
        self.db_handler = DatabaseHandler()

    def test_combine_string(self):
        input = ["Alpha","Beta","Gamma"]
        expected = "Alpha, Beta, Gamma"
        result = self.db_handler.combined_elements(input)
        self.assertEqual(expected,result)


    def test_select_single_data(self):
        tables = ["VarioProjects"]
        columns = ["Projekttitel", "Kurzbezeichnung", "Bauherr"]
        fetched_result = self.db_handler.select_data(tables,columns,where_clause="id = 23")
        result = list(fetched_result[0].keys())
        self.assertEqual(columns,result)

    def test_select_data(self):
        tables = ["VarioProjects"]
        columns = ["Projekttitel", "Kurzbezeichnung", "Bauherr"]
        fetched_result = self.db_handler.select_data(tables,columns)
        result = list(fetched_result)
        self.assertEqual(19,len(result))



    

    def tearDown(self):
        self.db_handler.close_connection()
        

    
        

if __name__ == "__main__":
    unittest.main()