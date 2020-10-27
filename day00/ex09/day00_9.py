import sys
import random

def main():
    x = random.randint(0,99)

    print("This is an interactive guessing game!" + "\n" + \
        "You have to enter a number between 1 and 99 to find out the secret number."  + "\n" + \
            "Type 'exit' to end the game." + "\n" +  "Good luck!")
    count = 1
    while True:

        a = input("What's your guess between 1 and 99?: ")
        
        if a == "exit":
            break
        elif int(a) == x:
            print("Congratulations, you've got it!")
            print("You won in " + str(count) +" attempts!")
            break
        elif int(a) > x:
            print("Too high!")
            print(count)
            
        elif int(a) < x:
            print("Too low!")
            print(count)
            
        elif a.isdigit() == False:
            print("That's not a number.")
        count += 1
        
    


if __name__ == '__main__':
    main()