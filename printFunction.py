from pwn import *
from termcolor import colored, cprint

def print_function(): 
	cprint( "\nEnter the", "yellow", end=" ")
	cprint( "File Path", "red", attrs=["bold","underline"], end=" ")
	cprint( "to search (ex files/bof3)", "yellow")
	file_path = input()
	
	cprint( "Enter any", "yellow", end=" ")
	cprint( "Function Name", "red", attrs=["bold","underline"], end=" ")
	cprint( "(ex win | N if none)", "yellow")
	function_name = input()
	
	elf = ELF(file_path)
	function_address = elf.symbols[function_name]
	print("\n",function_address)
	elf.close()
