#Найдите сумму элементов списĸа из задания 7
from random import randint
list = []
for i in range(16):
    list.append(randint(1, 100))
print(sum(list))