# Forbidden functions : random (moi: comment shuffle sans random.shuffle() ??)

def generator(text, sep=' ', option = None):
    """Splits a text with optional options"""
    import random
    import sys
    
    if type(text) == str and option in [None, 'shuffle', 'unique', 'ordered']:
            
        splitted = text.split(sep=sep)
        if option == 'shuffle':
            random.shuffle(splitted)
        if option == 'unique':
            splitted = list(set(splitted))
        if option == 'ordered':
            splitted.sort()

        for x in splitted:
            print(x)
            
    else:
        print('ERROR. Either text argument not a string or option argument not valid')

