import sys
import string

def text_analyzer(data = None):
    
	"""
	text_analyzer("Python 2.0, released 2000, introduced
	features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
	The text contains 143 character(s): - 2 upper letter(s)
	- 113 lower letter(s)
	- 4 punctuation mark(s)
	- 18 space(s)
	""" 
 
	if	not isinstance(data, str):
		print("AssertionError: argument is not a string")
		exit(1)
	while (data == None or not data or data == ""):
		data = input("Introcuce una cadena: ")
	num_upper = sum(1 for elem in data if elem.isupper())
	num_lower = sum(1 for elem in data if elem.islower())
	num_space = sum(1 for elem in data if elem.isspace())
	num_dot = sum(1 for elem in data if (elem in string.punctuation))
	print(f"- {num_upper} upper letter(s)\n- {num_lower} lower letter(s)\n- {num_dot} punctuation mark(s)\n- {num_space} space(s)")

if __name__ == "__main__":

	if (len(sys.argv) > 2):
		print("Incorrect arguments")
		exit(1)
	elif(len(sys.argv) == 1):
		text_analyzer()
	else:
		text_analyzer(sys.argv[1])