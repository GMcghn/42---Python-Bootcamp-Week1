from vector import *


v1 = Vector([0.0, 1.0, 2.0, 3.0])
print(v1.__dict__)

v11 = Vector([10.0, 5.0,  12.0, 3.0])


v2 = Vector(4)
print(v2.__dict__)

v22 = Vector(13)
print(v22.__dict__)

v3 = Vector((10,15))
print(v3.__dict__)


print(str(v1 / 3))
print(repr(v1 / 3))