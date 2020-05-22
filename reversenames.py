#!/usr/bin/env python3
import re

def reverse_names(names):
   
    pattern = r"^([\w .]+), ([\w .]+)$"
    reverse_names = re.search(pattern,names)
    return "{} {}".format(reverse_names[2],reverse_names[1])

#print(reverse_names("Skywalker, Luke"))
