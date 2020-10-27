import sys
if len(sys.argv)==2:

    import string
    count_upper = 0
    count_lower = 0
    count_space = 0
    count_punctuation = 0
    count_total = 0

    for i in range(len(sys.argv[1])):
        count_total+=1
        if sys.argv[1][i].isupper() == True:
            count_upper +=1
        if sys.argv[1][i].islower() == True:
            count_lower +=1
        if sys.argv[1][i].isspace() == True:
            count_space +=1
        #il faut rajouter les parenthèses sinon ça marche pas
        if (sys.argv[1][i] in string.punctuation) == True:
            count_punctuation +=1
    print(
            ("The text contains "+str(count_total)+" characters."),  \
            ("- "+str(count_upper)+" upper letters") , ("- "+str(count_lower)+" lower letters"), \
        ("- "+str(count_punctuation)+" punctuation marks") , ("- "+str(count_space)+" spaces") , sep='\n'*2)

if len(sys.argv)>2:
    
    print("only one parameter accepted")

if len(sys.argv)==1:

    print('No arguments provided.')