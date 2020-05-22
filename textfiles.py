#! /usr/bin/env python3
import os
import datetime
def readReadingList(path):
	textFile = open(path)
	firstLine =textFile.readline()
	print(firstLine)
	textFile.close()

#readReadingList("textFolder/readings.txt")

def readAllLines(path):
	with open(path) as file:
		for line in file:
			print(line.strip().lower())
			
#readAllLines("textFolder/readings.txt")


def linesList(path):
	textFile = open(path)
	textList = textFile.readlines()
	textFile.close()
	return textList

list = linesList("textFolder/readings.txt")
#print(list)

def getFileInformation(filename):
	absPath = os.path.abspath(filename)
	modifiyTime = os.path.getmtime(absPath)
	filesize =os.path.getsize(absPath)
	prettyTime = str(datetime.datetime.fromtimestamp(modifiyTime))
	return filesize,prettyTime

fsize, ptime = getFileInformation("textFolder/readings.txt")
print("Die Datei wurde am {0} gändert und ist {1} byte groß".format(ptime[0:10], fsize))