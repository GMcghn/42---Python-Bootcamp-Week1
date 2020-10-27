# RGB Red Green Blue
# cv2 uses numpy for manipulating images, so the proper and best way to get the size of an image is using numpy.shape.
#j'aurais pu utiliser PIL aussi

# moi je pense : [col:[[line][line]] col:[[line][line]]]
# Numpy images ici c'est en BGR et pas RGB ça change d'une fois à l'autre, bien vérifier
# et les 3 channels c'est BGR ou RGB

# quand string du path on met 'r' avant pour éviter les confusions avec les backslashslash dans le string
# r comme 'raw' string

# cv2.waitKey(0) must need, otherwise window is opened and closed instantly.

class ImageProcessor:


    def load(self, path):
        from cv2 import cv2
        im = cv2.imread(path)
        height, width = im.shape[0], im.shape[1]
        print("Loading image of dimensions ", height, " x ", width)
        return im

    def display(self, array):
        from cv2 import cv2
        cv2.imwrite(r'C:\Users\Gabriel\Desktop\Mes documents - Google Drive\DATA\19\day03\ex01\new_image.png', array)
        cv2.imshow('image name of the window', array)
        cv2.waitKey(0)