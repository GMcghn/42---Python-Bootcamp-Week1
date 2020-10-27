"""morse decoder"""

import os
import sys

MORSE_CODE_DICT	=	{ 
			'a':'.-', 'b':'-...', 
			'c':'-.-.', 'd':'-..', 'e':'.', 
			'f':'..-.', 'g':'--.', 'h':'....', 
			'i':'..', 'j':'.---', 'k':'-.-', 
			'l':'.-..', 'm':'--', 'n':'-.', 
			'o':'---', 'p':'.--.', 'q':'--.-', 
			'r':'.-.', 's':'...', 't':'-', 
			'u':'..-', 'v':'...-', 'w':'.--', 
			'x':'-..-', 'y':'-.--', 'z':'--..', 
			'1':'.----', '2':'..---', '3':'...--', 
			'4':'....-', '5':'.....', '6':'-....', 
			'7':'--...', '8':'---..', '9':'----.', 
			'0':'-----', ' ':'/'} 

def decrypt(string):
	
	morsed = ""
	for char in string:
		if char in MORSE_CODE_DICT.keys():
			morsed += MORSE_CODE_DICT[char]
			morsed += ' '
		else:
			morsed = "ERROR"
			print(morsed)
			break
	if morsed != "ERROR":
		print(morsed[:-3])
		
	

def main():
	
	string = ""
	for i in range(1, len(sys.argv)):
		string += sys.argv[i]
		string += " "
	decrypt(string.casefold())


if __name__ == "__main__":
	main()
