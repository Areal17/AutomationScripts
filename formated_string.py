#!/usr/bin/env python3

def luckyNumber(name):
	number = len(name) * 3
	result = "Hello {}, your lucky number is: {}".format(name,number)
	return result

print(luckyNumber("Ingo"))


def printPriceWithTax(price):
	tax = 1.19
	priceWithTax = price * tax
	result = "Netto: {:2f}€ mit MwSt.: {:.2f}€"
	return result.format(price,priceWithTax)
	
print(printPriceWithTax(156))

