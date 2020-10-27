"""kata01"""

import os
import sys

languages = {
	'Python': 'Guido van Rossum', 
	'Ruby': 'Yukihiro Matsumoto', 
	'PHP': 'Rasmus Lerdorf',
	}

def main():
	for key,value in languages.items():
		print(key + " was created by " + value)

if __name__ == "__main__":
	main()
