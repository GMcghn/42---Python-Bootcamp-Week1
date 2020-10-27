class Recipe:
    
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        import sys
        self.name = name
        levels = [1,2,3,4,5]
        if cooking_lvl in levels:
            self.cooking_lvl = cooking_lvl
        else:
             print("Error: set cooking level from 1 to 5")
             sys.exit(1)

        if cooking_time >= 0:
            self.cooking_time = cooking_time
        else:
            print("Error: no negative time")
            sys.exit(1)
        for ingredient in ingredients:
            if str(ingredient).isdigit() == True:
                print("Error: only strings as ingredients")
                sys.exit(1)
        self.ingredients = ingredients 
                
        self.description = description

        types = ['starter', 'lunch' , 'dessert']
        if recipe_type in types:
            self.recipe_type = recipe_type
        else:
            print("Error: type needs to be either “starter”, “lunch” or “dessert”")
            sys.exit(1)
    
    

    def __str__(self):
        #The __str__ method is useful for a string representation of the object, 
        # either when someone codes in str(your_object), or even when someone might do print(your_object). 
        # The __str__ method is one that should be the most human-readable possible, yet also descriptive 
        # of that exact object

        """Return the string to print with the recipe info"""
        t = ("Recipe name: ", self.name, "\n",             
        "Cooking level: ", str(self.cooking_lvl), "\n",
            "Cooking time: ", str(self.cooking_time), "\n",
            "List of ingredients: ", ', '.join(self.ingredients), "\n", 
            "Description: ", self.description, "\n", 
            "Recipe type: ", self.recipe_type)   

        #.join only takes one argument (tuple)
        txt = ''.join(t)        
        return txt
