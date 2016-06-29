#!/usr/bin/env python

from lxml import etree

with open("sample.html") as f:
    root = etree.fromstring(f.read())

print "\n" * 10
print etree.tostring(root, pretty_print=True)
print 'Prueba los siguientes comandos'
print '>>> print root.xpath(\'//div[@class="product"]\')'
print '>>> print root.xpath(\'//div[@class="product"]/img/@src\')'
print "### Reto: Intenta parsear los precios"