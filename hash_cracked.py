#!/usr/bin/python
#coding: utf-8

import requests
import sys
import re

url = 'http://hashtoolkit.com/reverse-hash?hash='
try:
	hasH = sys.argv[1]
except:
	print ("usage: python "+sys.argv[0]+" hash")
	sys.exit()
http = requests.get (url+hasH)

content = http.content
cracked = re.findall("<span title=\"decrypted (md5|sha1|sha256|sha384|sha512) hash\">(.*)</span", content) # expression relgular
print ("++++++++++++++++++ Hash Decrypter by GAD r00t ++++++++++++++++++")
print ("\n\t         (md5|sha1|sha256|sha384|sha512)")
print ("\n\t                  Algoritimo: "+cracked[0][0])
print ("\t               Password Cracked: "+cracked[0][1])
print ("\n                    www.facebook.com/m0gad")
print ("\n                    www.linkedin.com/in/mogad77")
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
