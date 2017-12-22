import socket
import sys
import argparse

def port_scanner(url, port):
	try:
		print ("[+] Test socket connecting to: " + url + ":" + str(port))
		s = socket.socket()
		s.connect((url,int(port)))
		s.send('test socket connection \n')
		banner = s.recv(1024)
		if (banner):
			print ("[+] Port " + str(port) + " open [+] \n" + banner)
			s.close()
	except:
		pass

def repeater(url, port, endPort):
	i = 0
	while (i < endPort):
		port_scanner(url, port)
		i += 1

def main():
	parser = argparse.ArgumentParser(description = "Help menu for PyNet port scanner")
	parser.add_argument("-u","--url", type=str, required = True) #url
	parser.add_argument("-p","--port", type=int, required = True) #port
	parser.add_argument("--endport", type=int, nargs = "?", required = False, default = None) #port end range
	args = vars(parser.parse_args())

	if (args['endport'] == None):
		port_scanner(args['url'], args['port'])
	else:
		repeater(args['url'], args['port'], args['endport'])

if (__name__ == "__main__"):
	main()