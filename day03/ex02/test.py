from ScrapBooker import ScrapBooker
from cv2 import cv2

path = r'C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day03\ex01\42AI.png'

im = cv2.imread(path)
dimensions = (2,4)
abc = ScrapBooker()

a = abc.juxtapose(im, dimensions[0], 1)
b = abc.juxtapose(a, dimensions[1], 0)

cv2.imwrite(r'C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day03\ex01\new_image.png', b)
cv2.imshow('image name of the window', b)
cv2.waitKey(0)
