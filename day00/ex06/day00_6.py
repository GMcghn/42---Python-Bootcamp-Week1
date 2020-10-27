import sys
import day00_6_functions 


def main():
    print("Please select an option by typing the corresponding number:" ,"\n", \
            "1: Add a recipe (name, ingredients, meal, prep_time)" ,"\n",\
            "2: Delete a recipe" ,"\n", \
            "3: Print a recipe" ,"\n", \
            "4: Print the cookbook" ,"\n", \
            "5: Quit")
    
    while True:

        x = input()
        #need to be a string
        if x == "1":
            print("Please enter the recipe's name, ingredients, meal, prep_time (with a space between each element):")
            a, b, c, d = input().split()
            day00_6_functions.add_recipe(a,b,c,d)
            
        elif x == "2":
            
            z = input("Please enter the recipe's name you want to remove from the cookbook: ")
            day00_6_functions.delete_recipe(z)
        elif x == "3":
            y = input("Please enter the recipe's name to get its details: ")
            day00_6_functions.print_recipe(y)
        elif x == "4":
            day00_6_functions.print_cookbook()
        elif x == "5":
            print("Cookbook closed.")
            break
        else:
            print("This option does not exist, please type the corresponding number.")
            print("To exit, enter 5.")





if __name__ == '__main__':
    main()