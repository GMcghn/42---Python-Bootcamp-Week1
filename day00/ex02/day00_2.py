import sys
if len(sys.argv)==2:

    number = int(sys.argv[1])
    if number == 0:
        print("zero")
    elif number%2 == 0:
        print("even")
    elif number%2 == 1:
        print("odd")
    

if len(sys.argv)>2:
    
    print("only one parameter accepted")

if len(sys.argv)==1:

    print('No arguments provided.')