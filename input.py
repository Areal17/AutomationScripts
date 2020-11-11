#!/usr/bin/env python3
import sys
import re


def simpleInput():
    """Simple function"""
    text = input("Gib mal einen Text ein ")
    output = "Hey - du hast \"" + text + "\" eingegeben"
    print(output)


def getMailAdress():
    text = input("Geben sie Ihre E-Mail-Adresse ein: ")
    pattern = r"^[\w\-._\d]+@[\w.\-]+\.[a-z]{2,3}$"
    email = re.search(pattern, text)
    if email is None:
        print("Oh oh")
        sys.exit(1)
    else:
        print("Hallo! Ihre Mail-Adresse lautet: \"" + text + "\"")


getMailAdress()