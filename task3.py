#Создайте пустой списоĸ и добавьте в него 10 случайных чисел и выведите их. В
#данной задаче нужно использовать фунĸцию randint.

from random import randint
list = []
for i in range(10):
    list.append(randint(1, 10))
print(list)