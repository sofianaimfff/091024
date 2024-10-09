#Создайте списоĸ из случайных чисел и найдите наибольший элемент в нем.
from random import randint
list = []
for i in range(16):
    list.append(randint(1, 100))
list.sort()
print(list[-1])