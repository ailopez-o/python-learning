import sys

if (not (len(sys.argv) == 3)):
	print("AssertionError: too many arguments")
	exit(1)
try:
	a = (int)(sys.argv[1])
	b = (int)(sys.argv[2])
except ValueError:
	print("AssertionError: only integers")
	exit(1)
print('{:<28}{}'.format("Sum" , a + b))
print('{:<28}{}'.format("Difference", a - b))
print('{:<28}{}'.format("Product", a * b))
try:
	print('{:<28}{}'.format("Quotient", a / b))
	print('{:<28}{}'.format("Reminder", a % b))
except:
	print('{:<28}{}'.format("Quotient", "ERROR (division by zero)"))
	print('{:<28}{}'.format("Reminder", "ERROR (modulo by zero)"))
