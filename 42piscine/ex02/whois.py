import sys

if __name__ == "__main__":

	if (len(sys.argv) > 2):
		print("AssertionError: more than one argument are provided")
		exit()
	try:
		num = (int)(sys.argv[1])
	except ValueError:
		print ("Is not a number")
		exit(1)
	if (num == 0):
		print("I'm Zero.")
	elif (num % 2) == 0:
		print("I'm Even.") 
	else:
		print("I'm Odd.")
  