"""removes all the words in a string that are shorter than or equal to n letters, and returns the filtered list with no punctuation."""

import sys
import os

punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""

def strippunc(string):

	nopunc = ""
	for char in string:
		if char not in punctuations:
			nopunc += char
	return nopunc

def filterwords(string, nb):
	
	nopunc = strippunc(string)
	tab = nopunc.split()
	new_list = [word for word in tab if len(word) >= nb]
	if len(new_list) > 0:
		print(new_list)
	else:
		print("The list is empty !")

def main():
	
	if len(sys.argv) == 3:
		try:
			nb = int(sys.argv[2])
			filterwords(sys.argv[1], nb)
		except ValueError:
			print("Second arg isn't a valid number")
	else:
		print("There has to be 2 args")

if __name__ == "__main__":
	main()
