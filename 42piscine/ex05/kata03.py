kata = "The right format"

if (not isinstance(kata, str) or len(kata) > 42):
	exit (print("Wrong Format"))
print ("-" * (41 - len(kata)) + kata)