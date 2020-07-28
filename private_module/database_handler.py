import os
import sys
import mysql.connector
import private_module.credetials as credetials



class DatabaseHandler:
    connection = None

    # def __init__(self):
    #     """ Initializer. Create connection to database. The credetials are stored in credetial.py where implemented the credetial_for_db() function """
    #     the_host, the_user, the_password, the_database = credetials.credetials_for_db()
    #     try:
    #         self.connection = mysql.connector.connect(host=the_host,user=the_user,password=the_password,database=the_database,use_pure=True)
    #     except mysql.connector.Error as err:
    #         if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR_WITH_PASSWORD:
    #             print("something is wrong with username or password")
    #         elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    #             print("database don't exists")
    #         else:
    #             print(err)

    def __init__(self,the_host,the_user,the_password,the_database):
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
        """ tables and columns as list, where clause as string (without WHERE) and join_clause as string (without JOIN or LEFT JOIN) """
        cursor = self.connection.cursor(dictionary=True)
        tables_string = self.combined_elements(tables)
        colls_string = self.combined_elements(colls)
        join_string = "LEFT JOIN " + join_clause if join_clause != None else ""
        where_string = "WHERE " + where_clause if where_clause != None else ""
        result = []
        query = "SELECT {colls} FROM {tables} {join} {where}".format(colls=colls_string,tables= tables_string,join=join_string,where=where_string)
        print(query)
        cursor.execute(query)
        # for-lop needed because cursor.close()
        for row in cursor:
            result.append(row)
        cursor.close()
        return result
    

    def select_data_from_string(self,query_string):
        """ Use this, when the query is complex. The Argument is a string """
        result = []
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query_string)
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def select_test_data(self):
        cursor = self.connection.cursor()
        result = []
        query = ("SELECT AZii3, Kurzbezeichnung, Projektstandort FROM VarioProjects ")
        cursor.execute(query,2)
        for (AZii3, Kurzbezeichnung, Projektstandort) in cursor:
            result.append((AZii3, Kurzbezeichnung, Projektstandort))
        cursor.close()
        return result


    def close_connection(self):
        """ Close the Mysql Connection """
        self.connection.close()