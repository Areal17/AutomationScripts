#!/usr/bin/env python3
import requests
import bs4 as bs 
import lxml

the_URL = "https://de.wikipedia.org/wiki/Liste_der_börsennotierten_deutschen_Unternehmen"
response = requests.get(the_URL)

# mit nur einem ul - Element
soup_Object = bs.BeautifulSoup(response.text,'lxml')
# lists = soup_Object.find('ul')
# list_Rows = []

# for row in lists.findAll('li')[0:]:
#     list_Rows.append(row.text)

# print(list_Rows)

lists = soup_Object.findAll('ul',{'id':'','class':''}) # lists ist ein sog. ResultSet - Es sollen nur die Ergebniss ohne class oder id berücksichtigt werden
for list in lists:
    print(len(list))

