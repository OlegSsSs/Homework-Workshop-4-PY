# Задача 22.
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого набора. m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# Output:
# 6 12

import random
a = int(input('Введите количество чисел в 1-ом наборе: '))
l =[]
for num in range(0,a):
    random_number = round(random.randint(0,10))
    l.append(random_number)
print(l)
x = set(l)

b = int(input('Введите количество чисел во 2-ом наборе: '))
m =[]
for num in range(0,b):
    random_number = round(random.randint(0,10))
    m.append(random_number)
print(m)
y = set(m)
c = x.intersection(y)
if x.isdisjoint(y):
    print('Наборы чисел не пересекаются')
else:
     print('Повторяющиеся числа в наборах: ', c)
