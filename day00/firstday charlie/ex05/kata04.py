"""kata04"""

import os
import sys

t = (0, 4, 132.42222, 10000, 12345.67)

def main():
	sn1 = "{0:.2e}".format(t[3])
	sn2 = "{0:.2e}".format(t[4])
	print("day_%02d, ex_%02d : %.2f, %s + %s" % (t[0], t[1], t[2], sn1, sn2))


if __name__ == "__main__":
	main()
