def what_are_the_vars(*args, **kwargs):
    """Your code"""
    obj = ObjectC()
    if len(args)+ len(kwargs) == 0:
        return obj
    else:
        if len(kwargs)>0:

            for key, value in kwargs.items():
                if "var" in str(key):
                    obj = None
                    break
                else:
                    setattr(obj, key, value)


                i = 0
                for arg in args:
                    t = ("var", str(i))
                    a = "".join(t)
                    setattr(obj, a, arg)
                    i += 1
        else:
            i = 0
            for arg in args:
                t = ("var", str(i))
                a = "".join(t)
                setattr(obj, a, arg)
                i += 1
        

        return obj
    
    

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    # print(obj)
    # print(dir(obj))
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)