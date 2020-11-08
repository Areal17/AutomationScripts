#!/usr/bin/env python3
import os
import sys
import re

def clean_text(filepath):
	with open(filepath,"r+") as file:
		new_text = ""
		tag_regex = re.compile(r'#{1}[a-zA-Z/0-9-]+')
		for line in file:
			checked_text = tag_regex.sub("",line)
			new_text += checked_text
		file.write(new_text)
		
	

if __name__ == "__main__":
	arguments = sys.argv
	if len(arguments) <= 1:
		print("Pfadname fehlt")
		sys.exit(1)
	file_name = arguments[1]
	clean_text(file_name)
	