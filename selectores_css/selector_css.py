#!/usr/bin/env python

with open('sample.html') as f:
    html_doc = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print "\n" * 10
print(soup.prettify())
print "Prueba los siguientes comandos:"
print '>>> print soup.select("div > span")'
print '### Reto obten los precios'