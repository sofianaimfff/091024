#Создайте списоĸ из случайных чисел. Найдите маĸсимальное ĸоличество его
#одинаĸовых элементов.

from random import randint
list = []
for i in range(16):
    list.append(randint(1, 100))
print("максимальное количество одинаковых элементов списка равно количество элементов в этом списке")