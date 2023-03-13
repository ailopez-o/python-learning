import sys

if __name__ == "__main__":

	if (len(sys.argv) > 2):
		exit(print("AssertionError: more than one argument are provided"))
	try:
		num = (int)(sys.argv[1])
	except ValueError:
		exit(print ("Is not a number"))
	if (num == 0):
		print("I'm Zero.")
	elif (num % 2) == 0:
		print("I'm Even.") 
	else:
		print("I'm Odd.")
  