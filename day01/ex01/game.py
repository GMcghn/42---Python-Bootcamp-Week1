class GotCharacter:
# https://www.w3schools.com/python/python_inheritance.asp

    def __init__(self, first_name, is_alive = True):
        #properties (ne doivent pas forcément être en attributes)
        self.first_name = first_name
        self.is_alive = is_alive

# Inheritance allows us to define a class that inherits all the methods and properties from another class
# To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class
class Lannister(GotCharacter):
    """ class representing the Lannister family. Definitely the most badass of the saga. """

    # When you add the __init__() function, the child class will no longer 
    # inherit the parent's __init__() function.
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
    # Python also has a super() function that will make the child class inherit all the methods and properties from its parent
    def __init__(self, first_name, family_name = 'Lannister', house_words = "A Lannister always pays his debts."):
        self.family_name = family_name
        self.house_words = house_words
        # no 'self'
        # define a value (is_alive) if not in child properties (first_name)
        super().__init__(first_name, is_alive = True)

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
        return self.is_alive

