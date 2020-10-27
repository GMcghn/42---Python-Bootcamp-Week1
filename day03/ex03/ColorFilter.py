# The term "unsigned" in computer programming indicates a variable that can hold only positive numbers. The term "signed" in computer code indicates that a variable can hold negative and positive values.
# Check whether your image is uint8 or not : image = image.astype(np.uint8) sinon ça peut faire foirer imshow
#   error genre python numpy multiply hpp:137: error: (-215:Assertion failed)


class ColorFilter:

    def invert(self, array):
        new_array = 255 - array
        # ALTERNATIVELY:  array = cv2.bitwise_not(array)
        return new_array

    def to_red(self, array):
        import numpy as np
        new_array = np.multiply(array, [0,0,1])
        new_array = new_array.astype(np.uint8)
        return new_array

    def to_blue(self, array):
        import numpy as np
        new_array = np.multiply(array, [1,0,0])
        new_array = new_array.astype(np.uint8)
        return new_array

    def to_green(self, array):
        import numpy as np
        new_array = np.multiply(array, [0,1,0])
        new_array = new_array.astype(np.uint8)
        return new_array
        
