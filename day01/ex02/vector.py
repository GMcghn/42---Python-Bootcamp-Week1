class Vector:
    """ Vector object builder to use for mathematical purposes """
    # https://rszalski.github.io/magicmethods/
    import numpy as np

    def __init__(self, d_values):

        
        if isinstance(d_values, list) == True:
            self.d_values = d_values
            self.size = len(d_values)
        elif str(d_values).isdigit() == True:
            self.d_values = [x for x in range(d_values)]
            self.size = d_values
        elif isinstance(d_values, tuple) == True and len(d_values) == 2:
            self.d_values = [x for x in range(d_values[0],d_values[1])]
            self.size = d_values[1] - d_values[0]
        
        else:
            print("ERROR: Use as Vector attribute either a list, a single number or a tuple")
    

    def __add__(self, other):
        #The others gave examples how to do this in pure python. If you want to do this with arrays with 100.000 elements, you should use numpy"
        if isinstance(other, Vector) == True:
    
            if self.size == other.size:
                sum = map(lambda x, y: x+y, self.d_values, other.d_values)
                vectors_sum = Vector(list(sum))
                return(vectors_sum)

            else: 
                return("ERROR: Vectors don't have the same size")

        elif str(other).isdigit() == True:
            sum = [x + other for x in self.d_values]
            vectors_sum = Vector(list(sum))
            return(vectors_sum)

    """So, all of these magic methods do the same thing as their normal equivalents, except the perform 
    the operation with other as the first operand and self as the second, rather than the other way around. 
    In most cases, the result of a reflected operation is the same as its normal equivalent, so you may 
    just end up defining __radd__ as calling __add__ and so on. Note that the object on the left hand side 
    of the operator (other in the example) must not define (or return NotImplemented) for its definition 
    of the non-reflected version of an operation. For instance, in the example, some_object.__radd__ will 
    only be called if other does not define __add__.
    """     
    def __radd__(self, other):
        return (self + other)

    def __str__(self):
        return str(self.d_values)

    # https://www.geeksforgeeks.org/str-vs-repr-in-python/
    def __repr__(self):
        return repr(self.d_values)

    def __sub__(self, other):
       
        if isinstance(other, Vector) == True:
    
            if self.size == other.size:
                substraction = map(lambda x, y: x-y, self.d_values, other.d_values)
                vectors_sub = Vector(list(substraction))
                return(vectors_sub)

            else: 
                return("ERROR: Vectors don't have the same size")

        elif str(other).isdigit() == True:
            substraction = [x - other for x in self.d_values]
            vectors_sub = Vector(list(substraction))
            return(vectors_sub)
        
    def __rsub__(self, other):
        
        if isinstance(other, Vector) == True:
    
            if self.size == other.size:
                substraction = map(lambda x, y: y-x, self.d_values, other.d_values)
                vectors_sub = Vector(list(substraction))
                return(vectors_sub)

            else: 
                return("ERROR: Vectors don't have the same size")

        elif str(other).isdigit() == True:
            substraction = [other - x for x in self.d_values]
            vectors_sub = Vector(list(substraction))
            return(vectors_sub)

    def __truediv__(self, other):

        if str(other).isdigit() == True:
            division = [x / other for x in self.d_values]
            vectors_div = Vector(list(division))
            return(vectors_div)

        else: 
            return("ERROR: divider can only be one number")

    def __rtruediv__(self, other):
        import sys
        if str(other).isdigit() == True:
            try:
                division = [other / x for x in self.d_values]
            except ZeroDivisionError:
                print("ERROR: 0 divider")
                sys.exit(1)
                
            vectors_div = Vector(list(division))
            return(vectors_div)

        else: 
            return("ERROR: divider can only be one number")
    
    def __mul__(self, other):

        # dot product =: vector*vector = scalar
        if isinstance(other, Vector) == True:
            
            if self.size == other.size:
                multi = map(lambda x, y: x*y, self.d_values, other.d_values)
                vectors_mul = Vector(list(multi))
                return(vectors_mul)

            else: 
                return("ERROR: Vectors don't have the same size")

        elif str(other).isdigit() == True:
            multi = [x * other for x in self.d_values]
            vectors_mul = Vector(list(multi))
            return(vectors_mul)

    def __rmul__(self, other):
        return (self * other)

        
            


        
        