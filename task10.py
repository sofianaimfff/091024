#Найдите среднее арифметичесĸое элементов списĸа из задания 7
from random import randint
list = []
for i in range(16):
    list.append(randint(1, 100))
(sum(list))//16
print((sum(list))//16)