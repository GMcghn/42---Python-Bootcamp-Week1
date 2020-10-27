# not finished mais il est badant alors en suspends

# Check out the dir function.
# dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)
# ex :['ID_COUNT', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'id', 'name', 'transfer', 'value']
#WARNING: YOU WILL HAVE TO MODIFY THE INSTANCES’ ATTRIBUTES IN ORDER TO FIX THEM.


# in the_bank.py
class Account():
# In Python 3: inherit from object if you are writing code that tries to be Python agnostic, that is, it needs to work both in Python 2 and in Python 3. Otherwise don't, it really makes no difference since Python inserts it for you behind the scenes.

    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
             self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank():
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """


        # is corrupted if
        if isinstance(origin, Account) == False or isinstance(dest, Account) ==False:
            print("CORRUPTED: wrong object")
            return False
        
        if len(origin.__dict__) %2 == 0 or len(dest.__dict__) %2 == 0:
            print("CORRUPTED: uneven amount of attributes")
            return False
        
        for x in origin.keys():
            if x[0] == 'b':
                print("CORRUPTED: origin attribute starts with a 'b'")
                return False
        
        for x in dest.keys():
            if x[0] == 'b':
                print("CORRUPTED: dest attribute starts with a 'b'")
                return False
        
        if not ('zip' in [str(x[0:3]) for x in origin.keys()] and 'attr' in [str(x[0:4]) for x in origin.keys()]):
            print("CORRUPTED: no 'zip' or 'attr'")
            return False
        
        if not ('zip' in [str(x[0:3]) for x in dest.keys()] and 'attr' in [str(x[0:4]) for x in dest.keys()]):
            print("CORRUPTED: no 'zip' or 'attr'")
            return False

        if not (
                'name' in [str(x[0:3]) for x in origin.keys()] and 
                'id' in [str(x[0:4]) for x in origin.keys()] and
                'value' in [str(x[0:4]) for x in origin.keys()]
                ):
            print("CORRUPTED: no 'name' or 'id' or 'value' in origin")
            return False

        if not (
                'name' in [str(x[0:3]) for x in dest.keys()] and 
                'id' in [str(x[0:4]) for x in dest.keys()] and
                'value' in [str(x[0:4]) for x in dest.keys()]
                ):
            print("CORRUPTED: no 'name' or 'id' or 'value' in dest")
            return False

        ###################################
        if amount < 0:
            print("ERROR: transaction is invalid if amount < 0 ")
            return False
        
        # print(self.account)
        a = 0
        b = 0
        for x in self.account:
            # print(x.name, x.id)
            # print(origin == x.id or origin == x.name)
            if origin == x.id or origin == x.name:
                # print(x.value)
                a = 1
                if amount > x.value:
                    print("ERROR: the amount is larger than the funds the first account has available")
                    return False
                else:
                    for y in self.account:
                        # print(y.name, y.id)
                        # print(dest == y.id or dest == y.name)
                        if dest == y.id or dest == y.name:
                            x.value -= amount
                            y.value += amount
                            b = 1
                            return True
                    if b == 0:              
                        print("ERROR: dest account : wrong identifier or  not present in Bank")
                        return False    
        if a == 0:              
            print("ERROR: origin account : wrong identifier or  not present in Bank")
            return False
            
                        
        



    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        pass
