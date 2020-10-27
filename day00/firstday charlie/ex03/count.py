"""Module docstring : this module is purely for learning python"""

import sys
import os

def	text_analyzer(s = ""):

	"""Function docstring : the purpose of this function is to analyze strings"""

	if (len(s) == 0):
		print("What is the text to analyze ?")
	
	else:
		up, low, punc, spaces, char = 0, 0, 0, 0, 0
		for i in s:
			if i.isupper():
				up += 1
			elif i.islower():
				low += 1
			elif i == ' ':
				spaces += 1
			elif i.isnumeric():
				pass
			else:
				punc += 1
			char += 1
		print("The text contains " + str(char) + " characters:\n")
		print("- " + str(up) + " upper letters\n")
		print("- " + str(low) + " lower letters\n")
		print("- " + str(punc) + " punctuation marks\n")
		print("- " + str(spaces) + " spaces")
