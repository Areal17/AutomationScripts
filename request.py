#! /usr/bin/env python3
import requests
import socket

def check_connectivity(adress):
	request = requests.get(adress)
	statusCode = request.status_code
	return statusCode

def getHeaderForAdress(adress):
	request = requests.get(adress)
	header = request.headers
	return header

print(check_connectivity("https://vario.f4.htw-berlin.de"))
print(getHeaderForAdress("https://vario.f4.htw-berlin.de"))
