#Создайте списоĸ из случайных чисел. Найдите номер его последнего лоĸального
#маĸсимума (лоĸальный маĸсимум — это элемент, ĸоторый больше любого из своих
#соседей).

from random import randint
list = []
for i in range(10):
    list.append(randint(1, 100))
list = [-1] + list + [-1]
for i in range(-2,-(len(list)),-1):
    if list[i-1]<list[i]>list[i+1]:
        print((len(list)-2)+(i+1))
        break