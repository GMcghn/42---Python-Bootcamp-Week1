
# NOTE : All those methods can be implemented in one line. You only need to find the right NumPy functions.
# numpy.asarray : Input data, in any form that can be converted to an array. This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays.

class NumPyCreator:
    


    def from_list(self, lst, datatype=None):
        import numpy as np
        x = np.asarray(lst, dtype = datatype)
        return x

    def from_tuple(self, tpl, datatype=None):
        import numpy as np
        x = np.asarray(tpl, dtype = datatype)
        return x

    def from_iterable(self, itr, datatype=None):
        import numpy as np
        x = np.array([])
        for i in itr:
            x = np.append(x,i)
        return x


    def from_shape(self, shape, value=0, datatype=None):
        import numpy as np
        x = np.full(shape,value)
        return x


    def random(self, shape, datatype=None):
        import numpy as np
        x = np.random.random(shape)
        return x

    def identity(self, n, datatype=None):
        import numpy as np
        x = np.eye(n)
        return x