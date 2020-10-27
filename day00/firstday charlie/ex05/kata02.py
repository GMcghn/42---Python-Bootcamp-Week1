"""kata02"""

import os
import sys

t = (3,30,2019,9,25)

def main():
	print("%02d/%02d/%04d %02d:%02d" % (t[4],t[3],t[2],t[0],t[1]))

if __name__ == "__main__":
	main()
