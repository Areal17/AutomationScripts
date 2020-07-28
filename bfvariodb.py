#!/usr/bin/env python3

import os
import sys
import mysql.connector
import private_module.database_handler as db



if __name__ == "__main__":
    database_handler = db.DatabaseHandler()
    #input = ("SELECT Projekttitel, Kurzbezeichnung FROM VarioProjects")
    #result = database_handler.select_test_data()
    query = ("SELECT AZii3, Kurzbezeichnung, Projektstandort FROM VarioProjects "
                 "WHERE id={}".format(23))
    result = database_handler.select_data_from_string(query)

    for (AZii3, Kurzbezeichnung, Projektstandort) in result:
        print("{} - {} - {}".format(AZii3, Kurzbezeichnung, Projektstandort))

    