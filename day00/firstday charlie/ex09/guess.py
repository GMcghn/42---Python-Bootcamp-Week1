"""A bit like a lottery game"""

import os
import sys
import random

def main():


	i = 0
	hidden = random.randrange(1, 101)
	print("Welcome to the casino ! You have to guess the number chosen randomly between 1 and 100")
	while 1:
		while 1:
			try:
				guess = int(input("Please enter your guess: (0 to exit) "))
				break
			except ValueError:
				print("This isn't a valid number, try again")

		if guess == 0:
			i = -1
			break
		elif guess == hidden:
			i += 1
			break
		elif guess < hidden:
			print("Your guess is too low")
			i += 1
		elif guess > hidden:
			print("Your guess is too high")
			i += 1
	
	if i == -1:
		print("Bye bye loser !")
	elif i == 1:
		if hidden == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		print("Congratulations! You got it on your first try!")	

	else :
		print("Touché ! bravo mister DeCoco")
		print("You won in " + str(i) + " attempts!")

if __name__ == "__main__":
	main()
