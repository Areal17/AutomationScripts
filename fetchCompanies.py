#!/usr/bin/env python3
import requests
import bs4 as bs 
import ssl
import lxml

theURL = "https://de.wikipedia.org/wiki/Liste_der_börsennotierten_deutschen_Unternehmen"
theContext = ssl.SSLContext()
response = requests.get(theURL)

soupObject = bs.BeautifulSoup(response.text,'lxml')
