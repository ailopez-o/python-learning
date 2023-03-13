# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for elem in kata:
	if (isinstance(elem, str) and isinstance(kata[elem], str)):
		print(f"{elem} was created by {kata[elem]}")
	else:
		print("format error")
