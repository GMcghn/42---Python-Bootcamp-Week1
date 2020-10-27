import sys
if len(sys.argv)>1:
    new_sentence = ''
    for args in sys.argv:
        new_word =''
        for y in range(len(args)):
            new_word += args[-(y+1)]
    
        new_sentence += new_word +' '
    print(new_sentence)

else:
    print('No arguments provided.')