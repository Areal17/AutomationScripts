#!/usr/bin/env python3
import os
import sys
import re

if sys.argv > 1:
    logfile = sys.argv[1]
    with open(logfile) as log_file:
        for line in log_file:
            line = line.strip()
            #hier kommt der Code rein, zum bearbeite / lesen der Zeile
            print(line)
else:
    print("Dateiname und Pfad fehlt")
    sys.exit(1)

def show_time_of_pid(line):
  """ Ausgegeben werden soll das Datum und die pid """
  pattern = r"(^[A-Z][a-z] +[\d\: ]+)(.+)([\d]{5})"
  result = re.search(pattern, line)
  return "{}pid:{}".format(result[1],result[3])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440


