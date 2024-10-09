#Найдите наименьший элемент в списĸе из задания 7
from random import randint
list = []
for i in range(16):
    list.append(randint(1, 100))
list.sort()
print(list[0])