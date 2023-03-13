kata = (19,42,21)

try:
	for	value in kata:
		(int)(value)
except ValueError:
    print(f"Formar Error")
    exit(1)
print("The 3 numbers are:", str(kata).replace('(', '').replace(')', ''))
	