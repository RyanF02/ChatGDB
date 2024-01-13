from termcolor import colored, cprint

# ***------------------------------***
#  This script is called by bruteForce
#  and is used to create a simple CLI 
#  to gather required data from users
# ***------------------------------***

def menu():	
	cprint( "\nEnter", "yellow", end=" ")
	cprint( "File Path", "red", attrs=["bold","underline"])
	executable = input()

	cprint( "Enter any", "yellow", end=" ")
	cprint( "Function Name", "red", attrs=["bold","underline"], end=" ")
	cprint( "to append (ex win | N if none)", "yellow")
	functionsuffix = input()

	cprint( "Enter any", "yellow", end=" ")
	cprint( "Hex Data", "red", attrs=["bold","underline"], end=" ")
	cprint( "to append (ex deadbeef | N if none)", "yellow")
	suffix = input()

	cprint( "Enter the", "yellow", end=" ")
	cprint( "Max Buffer Length", "red", attrs=["bold","underline"], end=" ")
	cprint( "to test (ex 100)", "yellow")
	maxlength = input()
	maxlength = int(maxlength)

	cprint( "Enter the", "yellow", end=" ")
	cprint( "Target Pattern", "red", attrs=["bold","underline"], end=" ")
	cprint( "to find (ex flag)", "yellow")
	expected_response = input()
	
	return executable, functionsuffix, suffix, maxlength, expected_response
