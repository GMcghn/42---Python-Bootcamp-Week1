class Book:
    from recipe import Recipe
    import datetime
    import sys
    # init method or constructor 
    def __init__(self, name, last_update, creation_date, recipes_list):
        
        import datetime
        self.name = name
        try:
            self.last_update = datetime.datetime.strptime(last_update,'%d/%m/%Y')
            self.creation_date = datetime.datetime.strptime(creation_date,'%d/%m/%Y')
        except ValueError:
            print("Error: For dates please use the following format : dd/mm/YYYY")
        self.recipes_list = recipes_list

        # for recipe in recipes_list:
        #     self.recipes_list.append(recipe.name)
        

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        from recipe import Recipe
        #isinstance()
        if isinstance(recipe, Recipe):

            # self.recipes_list.update({recipe.recipe_type : recipe})
            self.recipes_list[recipe.recipe_type].append(recipe)

            # update last_update
            import datetime
            self.last_update = datetime.datetime.now()

        else:
            print("The recipe object that you're trying to add doesn't have the right format")
        

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        a = [y for x in self.recipes_list.values() for y in x if y.name == name]
        for xx in a:
            print(xx)

        
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        
        a = [x.name for x in self.recipes_list[recipe_type]  ]
        for x in a:
            print(x)
            

    def __str__(self):
        
        # careful to the order of 'for' in list comprehension
        a = [recipe.name for type_meal in self.recipes_list.values() for recipe in type_meal ]
        # a = [y for x in self.recipes_list.values() for y in x]
        
        t = (
            self.name, self.last_update.strftime('%d/%m/%Y, %H:%M:%S'),
            self.creation_date.strftime('%d/%m/%Y, %H:%M:%S'), ', '.join(a)
            )
        text = '- '.join(t)
        return text


    
