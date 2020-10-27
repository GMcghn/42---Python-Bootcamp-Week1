import os
import sys

def	ft_check(n):
		if (n == 0):
			print("I'm Zero.")
		elif (n % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")


def	main():
	
	if (len(sys.argv) == 2):
		try:
			numb = int(sys.argv[1])
			ft_check(numb)
		except ValueError:
			print("ERROR")
		
	else:
		print("ERROR")

if __name__ == "__main__":
	main()
