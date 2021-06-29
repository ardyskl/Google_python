#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
	return hours*3600+minutes*60+seconds

print("Welcome to our little app")

cont = "y"
while(cont.lower() == "y"):
	hours = int(input("Enter number of hours: "))
	minutes = int(input("Enter number of minutes: "))
	seconds = int(input("Enter number of seconds: "))
	
	print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
	print()
	cout = input("Do you want to do another conversion? [y to continue] & [n to exit]: ")

	if cout == "n":
		print("Thanks for using this little app")
		quit()
