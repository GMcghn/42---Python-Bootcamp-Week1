import sys
import day00_4_functions

def main():
    
    if len(sys.argv)<3:
        print("Usage: python operations.py <number1> <number2>"  \
              + "\n" + "Example:" + "\n" +"\t" + "python operations.py 10 3")

    if len(sys.argv)>3:
        print("InputError: too many arguments")

    if len(sys.argv)==3:
        day00_4_functions.multiple_operations(sys.argv[1],sys.argv[2])
    

    

if __name__ == '__main__':
    main()