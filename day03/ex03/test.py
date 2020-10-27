from cv2 import cv2
from ImageProcessor import ImageProcessor
import numpy as np

from ColorFilter import ColorFilter

imp = ImageProcessor()

path = r'C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day03\ex01\42AI.png'
path2 = r'C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day03\ex01\capture.jpg'

im = cv2.imread(path)
im2 = cv2.imread(path2)

cf = ColorFilter()
# ab = cf.invert(im)
ab = cf.to_red(im)




cv2.imwrite(r'C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day03\ex01\new_image.png', ab)
cv2.imshow('image name of the window', ab)
cv2.waitKey(0)