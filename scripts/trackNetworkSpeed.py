'''
Version: 0.0.1_1 dev
Python Version: Python 3.5.2

Input: None
Output: Download speed by megabytes per second
		Log information into current directory.

'''

import time
import logging
import os

# Install psutil if it does not exist
try:
	import psutil
except ImportError:
	import subprocess
	subprocess.call("pip install --user psutil")

loggerFormat = "%(asctime)s:%(levelname)s:%(message)s" # TODO: set in config file
loggerPath = "/var/log/trackNetworkSpeed.log" # TODO: set in config file

# Create log file if it does not exist
try:
	if (os.path.isfile(loggerPath) == False):
		with open(loggerPath, 'xt') as file:
			file.write()
			file.close()
except:
	print("Unable to create log file. Exiting program.")

# Set logging configuration
logging.basicConfig(filename=loggerPath, level=logging.INFO, format=loggerFormat)

def log(multiLog):
	# check if needs to log to console and file
	try: multiLog
	except NameError:
		multiLog = None

	# allow log to console and file
	if (multiLog):
		console = logging.StreamHandler()
		console.setLevel(logLevel)
		console.setFormatter(logFormat)
		logging.getLogger("").addHandler(console)

class trackNetworkSpeed():
	def __init__(self):
		self.sleep_int = 1
		self.current_value = 0

	def calculateNetworkSpeed(self, sleep_int, current_value, speedBelowTrigger = 10):
		while True:
			get_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

			if (self.current_value):
				printSpeed(get_value - current_value)

			self.current_value = get_value

			if (unitConvert(get_value) < unitConvert(speedBelowTrigger)):
				logging.warning("{} bytes download speed below {}!").format(get_value, speedBelowTrigger)

			time.sleep(self.sleep_int)

	def unitConvert(value):
		return value/1024./1024./1024.*8

	def printSpeed(value):
		logging.info("{} gigabit download speed").format(value)
