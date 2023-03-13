import sys

if __name__ == "__main__":

	if (len(sys.argv) > 2):
		print("AssertionError: more than one argument are provided")
		exit()
	elif not sys.argv[1].isdigit():
		print("AssertionError: argument is not an integer")
	elif ((int)(sys.argv[1]) == 0):
		print("I'm Zero.")
	elif ((int)(sys.argv[1]) % 2 == 0):
		print("I'm Even.") 
	else:
		print("I'm Odd.")
  