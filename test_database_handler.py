#!/usr/bin/env python3
import unittest
from private_module.database_handler import DatabaseHandler
from private_module.credetials import credetials_for_db


class TestDatabaseHandler(unittest.TestCase):
    
    def setUp(self):
        host, user, password, database = credetials_for_db()
        self.db_handler = DatabaseHandler(host,user,password,database)

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

    def test_select_join(self):
        tables = ["VarioProjects"]
        columns = ["VarioProjects.Kurzbezeichnung", "VarioBuildingCosts.KG_300_t0", "VarioBuildingCosts.KG_300_t0"]
        join = "VarioBuildingCosts ON VarioProjects.id = VarioBuildingCosts.projectID"
        fetched_result = self.db_handler.select_data(tables,columns,join_clause=join)
        result = list(fetched_result)
        self.assertEqual(19,len(result))

    
    def test_select_string(self):
        query = """ SELECT
                        VarioBuildingCosts.KG_300_t3,
                        VarioBuildingCosts.KG_300_t2,
                        VarioBuildingCosts.KG_300_t1,
                        VarioBuildingCosts.KG_300_t0,
                        VarioBuildingCosts.KG_400_t3,
                        VarioBuildingCosts.KG_400_t2,
                        VarioBuildingCosts.KG_400_t1,
                        VarioBuildingCosts.KG_400_t0
                    FROM
                        VarioBuildingCosts
                    WHERE
                        VarioBuildingCosts.projectId = 7; """
        fetched_result = self.db_handler.select_data_from_string(query)
        result = list(fetched_result)
        self.assertEqual(1, len(result))

    

    def tearDown(self):
        self.db_handler.close_connection()
        

    
        

if __name__ == "__main__":
    unittest.main()