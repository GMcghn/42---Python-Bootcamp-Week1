

class ScrapBooker:


    def crop(self, array, dimensions, position=(0,0)):
        
        heigth, width = array.shape[0], array.shape[1]

        if dimensions[0] > heigth or dimensions[1] > width:
            print("ERROR dimensions too big")
        

        else:
            new_array = array[0:dimensions[0],0:dimensions[1]]
            return new_array

    def thin(self, array, n, axis):
        import numpy as np
        new_array = np.delete(array, n, axis)
        return new_array

    def juxtapose(self, array, n, axis):
        import numpy as np
        multiple_array = [array]*n
        concat_array = np.concatenate(multiple_array, axis=axis)
        return concat_array

    def mosaic(self, array, dimensions):
        from ScrapBooker import ScrapBooker
        a = self.juxtapose(array, dimensions[0], 1)
        b = self.juxtapose(a, dimensions[1], 0)
        return b





