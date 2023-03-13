kata = (2019, 9, 25, 3, 30)

try:
	for elem in kata:
		value = (int)(elem)
		if (value < 0):
			print ("Invalid numbers")
			exit(1)
except ValueError:
	print ("Invalid format")
	exit(1)
print(f"{kata[1]:02}/{kata[2]:02}/{kata[0]:04} {kata[3]:02}:{kata[4]:02}")