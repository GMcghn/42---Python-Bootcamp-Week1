import time
from random import randint
# https://medium.com/@vadimpushtaev/decorator-inside-python-class-1e74d23107f6

# ORDER MATTERS : le programme sera exécuté de haut en bas, si je mets log en dessous 
# de la classe il saura pas ce que c'est quand je l'appellerai dans l'instantiation
# A class body is executable code, which like all code is processed top to bottom.

class Decorators(object):

    #Occasionally (but not often), you really don't care about the object
    #  that your method is bound to, and in that circumstance, you can 
    # decorate the method with the builtin staticmethod() function to say so:
    #moi : classmethod marche pas ici masi staticmethod si
    @staticmethod
    def log(func):
                    
        def wrapped(*args, **kwargs):
            import time

            ts = time.time()
            result = func(*args, **kwargs)
            te = time.time()

            x = args[0]
            # x.log += (" World!\n")
            # print(x.log)


            a = str(func.__name__).split('_')
            b = [x.capitalize() for x in a]
            c = ' '.join(b)

            if ((te - ts)) > 1:
                x.log +=('Running: {} \t [ exec-time = {:5.3f} s ]'.format(c, (te - ts)) +"\n")
            else:
                x.log +=('Running: {} \t [ exec-time = {:5.3f} ms ]'.format(c, (te - ts)*1000) +"\n")

            
            return result
        return wrapped



class CoffeeMachine():  
    
    water_level = 100
    log = ''    
    
    @Decorators.log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @Decorators.log
    def boil_water(self):
        return "boiling..."

    @Decorators.log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @Decorators.log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
        

if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)

