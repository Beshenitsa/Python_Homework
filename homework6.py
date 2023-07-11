# Task 1. Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# first_number = int(input('Enter the first element of your arithmetic progression, please: '))
# difference =  int(input('Enter the difference: '))

# print('\n'. join(map(str, progression_list := [first_number + i * difference for i in range(int(input('Enter the amount of elements you woulf like to see: ')))]))) 


# Task 2. Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range_list = []

# lower_bound = int(input('Enter the lower bound of the range: '))
# upper_bound = int(input('Enter the upper bound of the range: '))

# for i in range(len(my_list)):
#     if my_list[i] > lower_bound and my_list[i] < upper_bound:
#         range_list.append(i)
# print(range_list)