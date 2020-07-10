from urllib.request import urlopen

url = "https://de.wikipedia.org/wiki/Liste_der_börsennotierten_deutschen_Unternehmen"
html = urlopen(url)
print(html.read())