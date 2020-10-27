from NumPyCreator import NumPyCreator
npc = NumPyCreator()

# a = npc.from_list([[1,2,3],[6,3,4]])
# a = npc.from_tuple(("a", "b", "c"))
# a = npc.from_iterable(range(5))

shape=(3,5)
# a = npc.from_shape(shape,2)

# a = npc.random(shape)
a = npc.identity(4)


print(a)
print(type(a))
