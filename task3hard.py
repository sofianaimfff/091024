#Создайте списоĸ из случайных чисел. Найдите второй маĸсимум.
from random import randint
list = []
for i in range(16):
    list.append(randint(1, 100))
list.sort()
print(list[-2])