#!/usr/bin/env python3

import os
import sys
import mysql.connector
import smtplib
import private_module.database_handler as db
import private_module.email_handler as email
from private_module.credetials import credetials_for_db
from private_module.credetials import credetials_for_userDB


def isTest():
    user_input = input("E-Mail versandt testen? True/False ")
    if user_input != 'True' and user_input != 'False':
        exit(-1)
    return bool(user_input)


if __name__ == "__main__":
    # test_mail = isTest()
    host, user, password, database = credetials_for_userDB()
    database_handler = db.DatabaseHandler(host,user,password,database)
    email_handler = email.EmailHandler()
    email_handler.sendMail()
    query = """ SELECT * FROM bfvariouser.VarioNewsletterRecipients
                WHERE isValidated = 1 && hasConfirm = 2 """
    fetched_result = database_handler.select_data_from_string(query)
    for row in fetched_result:
        # row ist ein Dictionary
        print("{} {}".format(row['token'],row['mail']))
    
    

    

    