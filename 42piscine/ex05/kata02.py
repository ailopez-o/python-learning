kata = (2019, 9, 25, 3, 30)

try:
	for elem in kata:
		value = (int)(elem)
		if (value < 0):
			exit(print ("Invalid numbers"))
except ValueError:
	exit (print ("Invalid format"))
print(f"{kata[1]:02}/{kata[2]:02}/{kata[0]:04} {kata[3]:02}:{kata[4]:02}")