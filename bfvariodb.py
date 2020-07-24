#!/usr/bin/env python3
# /Users/ingowie/Projekte/Übung/Python/bfvariodb.py
import os
import sys
import mysql.connector
from private_module import credetials
#from private_module.credetials_for_db import *
#modul = __import__("module")
host, user, password = credetials.credetials_for_db()

print(sys.path)

# host = "localhost"
# user = "root"
# password="schnickschnack"

# database = mysql.connector.connect(host=host,user=user,password=password)