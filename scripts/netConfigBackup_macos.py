#!/usr/bin/env python3

# run script as admin

import shutil
import datetime
import os
import zipfile
import sys
import types

def net_config_backup(networkConfigDirectory, createDir=False)
	if not (type(networkConfigDirectory) is list):
		networkConfigDirectory = ['/Library/Preferences/SystemConfiguration']

	configBackupPath = "./networkConfigBackup/"

	if not os.path.exists(configBackupPath):
		os.makedirs(configBackupPath)

	for directory in networkConfigDirectory:
		if not os.path.exists(directory):
			print("Path does not exist: " + directory)

			if (createDir == True):
				os.makedirs(directory)
				print("Successfully created directory: " + directory)
			else:	
				networkConfigDirectory.remove(directory)
				print("Removed path from list, restart program: " + directory)
				net_config_backup(networkConfigDirectory)

		now = str(datetime.datetime.now())

		if (not os.path.exists(now)):
			os.makedirs(now)
		elif (os.opath.exists(now)):
			now = now + "+1"
			os.makedirs(now)
		else:
			pass

		os.chdir(now)
		configBackupPath = configBackupPath + now
		try:
			shutil.copytree(directory, configBackupPath)
		except shutil.Error:
			print ("Run script as administrator\nExiting program...")
			sys.exit(1)

		os.chdir("../")
		shutil.make_archive(configBackupPath, 'zip', configBackupPath)