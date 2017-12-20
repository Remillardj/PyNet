'''
Version: 0.0.1 dev
Python Version: Python 3.5.2

Input: None
Output: Download speed by megabytes per second
		Log information into current directory.

'''

import time
import psutil
import logging

logging.basicConfig(filename="network_monitor.log",
					level=logging.INFO,
					format="%(asctime)s:%(levelname)s:%(message)s"
					)

class trackNetworkSpeed(object):
	def __init__(self):
		self.sleep_int = 1
		self.current_value = 0

	def calculateNetworkSpeed(self, sleep_int, current_value):
		while True:
			get_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

			if (self.current_value):
				printSpeed(get_value - current_value)

			self.current_value = get_value

			if (unitConvert(get_value) < unitConvert(10)):
				logging.warning("{} bytes download speed below 10!").format(get_value)

			time.sleep(self.sleep_int)

	def unitConvert(value):
		return value/1024./1024./1024.*8

	def printSpeed(value):
		logging.info("{} gigabit download speed").format(value)
