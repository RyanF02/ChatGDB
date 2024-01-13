import pyfiglet

from termcolor import colored, cprint

from bruteForceBuffer import brute_force 
from buildAPayload import build
from createShellcode import create_shellcode
from printFunction import print_function

# ***------------------------------***
#  This is the main script of the
#  ChatGDB A.E.G. program. It simply
#  outputs a selection menu to direct
#  users to more specific functions
#  across three sub scripts.
# ***------------------------------***

# Project Assumptions:
# - Correct User Input
# - Linux Executables (ELF)
# - 32 Bit Programs 

print(pyfiglet.figlet_format("ChatGDB"))
cprint( "How can I help?", "yellow")
cprint( "1 - Brute Force a Buffer", "magenta")
cprint( "2 - Build a Payload", "blue")
cprint( "3 - Attempt Simple Shellcode", "green")
cprint( "4 - Print Function Address", "red")
cprint( "(Please input 1, 2, 3, or 4)", "yellow")
user_choice = input()

match user_choice:
	case "1":
		brute_force()
	case "2":
		build()
	case "3":
		create_shellcode()
	case "4":
		print_function()
	case _:
		print('Error undefined input...')
