# import sys

# def main():
#     if len(sys.argv)<2:
#         print("not enough arguments")

#     else:
#         # list_0 = []
#         str = ''
#         for argv in sys.argv[1:]:
#             # list_0.append(argv)
#             str += argv + ' '
#         print("The 3 numbers are: " + str)

# if __name__ == '__main__':
#     main()

languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for key, value in languages.items():
    print(key + "was created by " +value)
            

   


