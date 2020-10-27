"""module doc"""
import os
import sys

def ft_operations(a, b):
	
	"""print the results of the four elementary mathematical 
	operations of arithmetic + the modulo op"""
	
	print("Sum:\t\t" + str(a + b))
	print("Difference:\t" + str(a - b))
	print("Product:\t" + str(a * b))
	if (b != 0):
		print("Quotient:\t" + str(a / b))
		print("Remainder:\t" + str(a % b))
	else:
		print("Quotient:\t" + "ERROR (div by zero)")
		print("Remainder:\t" + "ERROR (modulo by zero)")


def main():

	usage = "Usage: python operations.py <number1> <number2>\
		\nExample:\n\tpython operations.py 10 3"
	
	if (len(sys.argv) == 3):
		try:
			a = int(sys.argv[1])
			b = int(sys.argv[2])
			ft_operations(a, b)
		except ValueError:
			print("InputError: only numbers\n\n" + usage)
	elif len(sys.argv) > 3:
		print("InputError: too many arguments\n\n" + usage)
	else:
		print(usage)
		

if __name__ == "__main__":
	main()
