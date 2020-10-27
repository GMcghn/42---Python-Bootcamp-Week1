from recipe import Recipe
from book import Book
import datetime 

recipe_crepe = Recipe(
            "crepe", 2, 30, ['lait','farine', 'oeufs', 'sucre'], 
            "crepes: super comme goûter par ex", "dessert"
            )

recipe_chocolat = Recipe("chocolat", 4, 60, ['beurre de cacao','cacao', 'sucre'], 
            "chocolat cote d'or", "dessert")

listt = [recipe_crepe, recipe_chocolat]
#print(recipe_crepe)

book1 = Book('livre de cuisine1', '01/04/2020', '01/01/2020', 
            {'dessert': [recipe_crepe, recipe_chocolat], 'starter': [], 'lunch' :[]}
            )

# dict = {'dessert': [recipe_crepe, recipe_chocolat], 'starter': [], 'lunch' :[]}
# for type_meal in dict.values():
#     for recipe in type_meal:
#         print(recipe.name)
# a = [recipe.name for type_meal in dict.values() for recipe in type_meal ]
# print(a)
# listu = []
# for recipe in listt:
#     listu.append(recipe.name)
# print(listu)
recipe_salad = Recipe("salad", 1, 10, ['avocado','parsley', 'eggs'], 
            "frais et vege", "lunch")
recipe_salad2 = "hoho"
a = recipe_salad.recipe_type
# print(type(a))
b = 'dessert'

# print(book1.recipes_list['lunch'])
# print(type(book1.recipes_list))
# book1.recipes_list.update({a : recipe_salad})
# print(book1)
# book1.get_recipes_by_types('lunch')

# book1.get_recipe_by_name('chocolat')

book1.add_recipe(recipe_salad2)
# print(book1)



