#!/usr/bin/env python3
import requests
import bs4 as bs 
import lxml

wiki_url = "https://de.wikipedia.org/wiki/Liste_der_börsennotierten_deutschen_Unternehmen"
# Footer hat auch eine Liste. Diese wird mit ausgelesen - sie hat weder id noch class. 
# Börsennotiertes Unternehmen
# Deutscher Finanzmarkt
# Liste (deutsche Unternehmen)
# werden überflüssigerweise auch 

def fetch_website_at_url(the_URL):
    """ fetch website at given url. The text at the li tags will appen to list_rows. list_rows list is the return value"""
    response = requests.get(the_URL)
    soup_Object = bs.BeautifulSoup(response.text,'lxml')
    list_rows = []
    lists = soup_Object.findAll('ul',{'id':'','class':''}) # lists ist ein sog. ResultSet - Es sollen nur die Ergebniss ohne class oder id berücksichtigt werden
    for list in lists:
        lines = list.findAll('li')
        for line in lines:
            list_rows.append(line.text)
    return list_rows


companies = fetch_website_at_url(wiki_url)
for company in companies:
    print(company) 
print(len(companies))