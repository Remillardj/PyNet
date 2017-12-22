#!/usr/bin/env python3

// version 0.0.1 alpha prototype

import paramiko
import base64
import sys
import subprocess

sshJump = {['192.168.1.1', 22] : ['username', 'password'], ['192.168.1.2', 22] : 'pkey'}

def jumpSSH(pkey, ipaddress_ports[], username, password)
	sshJump = {}

	for hostname, port in sshJump:
		client = SSHClient()
		client.load_system_host_keys()
		client.connect(hostname, port)
	jumpSSH()