"""nested dictionnaries"""

import os
import sys

usage = "Please select an option by typing the corresponding number:\n\n\
	1: Add a recipe\n\
	2: Delete a recipe\n\
	3: Print a recipe\n\
	4: Print the cookbook\n\
	5: Quit"

def addRecipe(cookbook):

	recipe = input("What is the name of the recipe ?\t")
	ingredients = input("What are the ingredients ? (separated by commas)\t")
	while True:
		try:
			time = int(input("How much time is needed to cook this recipe (in minutes ?\t"))
			break
		except ValueError:
			print("That's not a valid number... Type an other one")
	meal = input("What kind of meal is it ?\t")
	cookbook[recipe] = {"ingredients" : ingredients, "meal" : meal, "time" : time}
	print("You've successfully added " + recipe + " !")

def delRecipe(cookbook):
	
	name = input("What recipe do you want to delete?\t")
	try:
		del cookbook[name]
		print("that recipe has been successfully deleted !\n")
	except KeyError:
		print("That recipe has not been found\n")

def printRecipe(cookbook):
	recipe = input("Please enter the recipe's name to get its details: ")

	if recipe in cookbook:
		print("Recipe for " + recipe + " : \n")
		print("\tIngredients list : " + cookbook[recipe]["ingredients"] +"\n")
		print("\tTo be eaten for " + cookbook[recipe]["meal"] + "\n")
		print("\tTakes " + str(cookbook[recipe]["time"])  + " minutes for cooking\n")
	else:
		print("There isn't that recipe in the cookbook...\n")


def printCb(cookbook):

	for names, infos in cookbook.items():
		print("\nRecipe name : ", names)

		for key in infos:
			print("\t" + key + ':', infos[key])
	print("\n")


def main():

	cookbook = {"sandwich" : {"ingredients" : "ham, bread, cheese, tomatoes", "meal" : "lunch", "time" : 10}, 
			"cake" : {"ingredients" : "flour, sugar, eggs", "meal" : "dessert", "time" : 60},
			"salad" : {"ingredients" : "avocado, arugula, tomatoes, spinach", "meal" : "lunch", "time" : 15}}
	
	while 1:
		
		print(usage)

		i = input()
		if i == "1":
			addRecipe(cookbook)
		elif i == "2":
			delRecipe(cookbook)
		elif i == "3":
			printRecipe(cookbook)
		elif i == "4":
			printCb(cookbook)
		elif i == "5":
			print("Cookbook closed")
			break
		else:
			print("This option does not exist, please type the corresponding number.")
			print("To exit, enter 5.")

if __name__ ==  "__main__":
	main()
