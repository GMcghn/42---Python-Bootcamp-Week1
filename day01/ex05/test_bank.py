from the_bank import *

a = Account('gabriel', value = 0)
a.transfer(1000)

b = Account('claire', value = 0)
b.transfer(2000)

KBC = Bank()

KBC.add(a)
KBC.add(b)

print(KBC.__dict__)
for x in KBC.account:
    print(x.__dict__)

print(KBC.transfer(1, 2, 1000))

print()
for x in KBC.account:
    print(x.__dict__)

print(dir(a))