import re
import sqlite3

# Beispiel für Reguläre Ausdrücke


def findPhoneNumber(input):
	phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
	mo = phoneNumberRegex.search(input)
	if mo == None:
		print("keine Nummer gefunden")
	else:
		print("Telefonnummer gefunden: " + mo.group())
	
#findPhoneNumber("Meine Nummer lautet: 444-666-900")

def findEmailAdress(input):
    # der Punkt zur Topleveldomain wird gecovert
	mailRegex = re.compile(r'[A-Za-z0-9.-_]+@[A-Za-z0-9-_]+\.[a-z]{2,3}')
	
	mo = mailRegex.search(input) 
	if mo == None:
		print("keine E-Mailadresse")
	else:
		print("Folgende Adresse gefunden \'" + mo.group(0) + "\'")
		
findEmailAdress("Adresse: ingo.wiederoder@areal-17.de")
# search ermittelt den ersten Treffer. Gäbe es mehrere Mail-Adressen und wollt man alle finden
# näme man findall()


def changeDateFormat(dateInput):
    # amerkikanisches Datum: 2020-03-13
    dateRegex = re.compile(r'(\d{4})-(\d{1,2})-(\d{1,2})')
    # es wird nach dem obigen Muster gesucht. \1 etc sind die Gruppen. Parameter 1 ist der ersetzte Text, Parameter 2 der Text, der durchsucht wird
    mo = dateRegex.sub(r'\3.\2.\1', dateInput)
    print(mo)
 
changeDateFormat("today is the 2020-03-13. It' a Friday")