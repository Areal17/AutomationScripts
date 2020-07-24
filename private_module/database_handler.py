import os
import sys
import mysql.connector
import private_module.credetials as credetials



class DatabaseHandler:
    connection = None

    def __init__(self):
        """ Initializer. Create connection to database. The credetials are stored in credetial.py where implemented the credetial_for_db() function """
        the_host, the_user, the_password, the_database = credetials.credetials_for_db()
        try:
            self.connection = mysql.connector.connect(host=the_host,user=the_user,password=the_password,database=the_database,use_pure=True)
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR_WITH_PASSWORD:
                print("something is wrong with username or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("database don't exists")
            else:
                print(err)

    
    def combined_elements(self,list_object):
        """ Combined elements in list_object to comma-separated string """
        num_of_elements = len(list_object)
        result = ""
        for i, element in enumerate(list_object):
            if i < num_of_elements - 1:
                result = result + element + ", "
            else:
                result = result + element
        return result

    
    def select_data(self,tables,colls=['*'],join_clause=None,where_clause=None):
        cursor = self.connection.cursor()
        tables_string = self.combined_elements(tables)
        colls_string = self.combined_elements(colls)
        result = None
        query = ("SELECT %s FROM %s "
                 "%s"
                 "WHERE %s")
        cursor.execute(query,(tables_string,colls_string,join_clause,where_clause))
        result = cursor
        cursor.close()
        return result
    

    def select_data_from_string(self,query_string):
        """ Use this, when the query is complex. The Argument is a string """
        result = None
        cursor = self.connection.cursor()
        cursor.execute(query_string)
        result = cursor
        cursor.close()
        return result

    def select_test_data(self):
        cursor = self.connection.cursor()
        result = []
        theID = 11
        # query = ("SELECT AZii3, Kurzbezeichnung, Projektstandort FROM VarioProjects "
        #          "WHERE id={}".format(theID))
        query = ("SELECT AZii3, Kurzbezeichnung, Projektstandort FROM VarioProjects ")
        cursor.execute(query,2)
        for (AZii3, Kurzbezeichnung, Projektstandort) in cursor:
            result.append((AZii3, Kurzbezeichnung, Projektstandort))
        return result


    def close_connection(self):
        """ Close the Mysql Connection """
        self.connection.close()