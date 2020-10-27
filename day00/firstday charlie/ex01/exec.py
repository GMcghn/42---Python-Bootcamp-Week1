import os
import sys

def	ft_alpha(string):
	alphastr = ""
	for i in string:
		if i.isupper():
			alphastr += i.lower()
		elif i.islower():
			alphastr += i.upper()
		else:
			alphastr += i
	return(alphastr)

def	ft_reverse(string):
	revstr = string[::-1]
	return (revstr)

def	main():
	string = ""
	for i in range(1, (len(sys.argv))):
		string += sys.argv[i]
		string += " "
	string = string[:-1]
	string = ft_alpha(string)
	string = ft_reverse(string)
	print(string)

if __name__ == "__main__":
	main()
