#Удалите все элементы из списĸа, созданного в задании 3

from random import randint
list = []
for i in range(10):
    list.append(randint(1, 10))
    list.pop(0)
print(list)
