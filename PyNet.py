import argparse
from modules import *



def banner():
    print ("#################################")
    print ("##     Help Menu for PyNet     ##")
    print ("#################################")

if (__name__ == "__main__"):
	parser = argparse.ArgumentParser(description='PyNet help menu')
	parser.add_argument('--tns', help='Track your networkspeed in Python')
	args = parser.parse_args()

banner()
if args.tns:
	result = trackNetworkSpeed.trackNetworkSpeed()
	print (result)