cookbook ={'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],'meal': 'lunch','prep_time': 10}, 
           'cake': {'ingredients': ['flour', 'sugar', 'eggs'],'meal': 'dessert','prep_time': 60} , 
           'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],'meal': 'lunch','prep_time': 15}}

def print_recipe(name):
        
    for key,value in cookbook.items():
     
        if key == name:
            print(value)

    # Charlie me dit plutot:
    # print(cookbook[name]) 
          
def delete_recipe(name):
    
    for key in cookbook.keys():
        if key == name:
            del cookbook[key]
            break

def add_recipe(name, ingredients, meal, prep_time):
    
    cookbook.update({name: {'ingredients': ingredients,'meal': meal, 'prep_time': prep_time}})

def print_cookbook():
    for key in cookbook.keys():
        print(key)



    
    
        