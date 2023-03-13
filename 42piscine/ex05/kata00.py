kata = (19,42,21)

try:
	for	value in kata:
		(int)(value)
except ValueError:
    exit(print(f"Formar Error"))
print("The 3 numbers are:", str(kata).replace('(', '').replace(')', ''))
	