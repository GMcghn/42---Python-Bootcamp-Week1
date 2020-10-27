from game import GotCharacter, Lannister
cersei = Lannister("Cersei")
print(cersei.__dict__)
cersei.print_house_words()
print(cersei.is_alive)
cersei.die()
print(cersei.is_alive)
print(cersei.__doc__)