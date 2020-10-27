"""printing elements of a tuple"""

import os
import sys

t = (19,42,21,36,58)

def main():
	string = "The " + str(len(t)) + " numbers are : "
	for i in t:
		string += str(i)
		string += ", "
	string = string[:-2]
	print(string)


if __name__ == "__main__":
	main()
