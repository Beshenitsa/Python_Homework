# Task 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# import numpy as np
# size = int(input("Input the amount of coins, please: "))
# array_of_coins = (np.random.randint(0, 2, size))
# print(array_of_coins)
# heads = int(np.sum(array_of_coins))
# tails = size - heads
# print(f"There are {heads} heads and {tails} tails.")
# if heads < tails:
#     print(f"So the minimum amount of coins we have to turn over is {heads}.")
# else:
#     print(f"So the minimum amount of coins we have to turn over is {tails}.")

# Task 2. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# sum = int(input("Please, input sum of the elements: "))
# product = int(input("Please, input product of the elements: "))

# x = (sum-int((sum**2-4*product)**0.5))//2
# y = (sum+int((sum**2-4*product)**0.5))//2

# print(x)
# print(y)

# Task 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# borderNumber = int(input("Input the border number, please: "))

# intPowerOfTwo = int(1)
# listOfPowersOfTwo = []

# if borderNumber < 2:
#     print("Sorry, the number you've dialed is too small.")
# else:
#     while intPowerOfTwo < borderNumber:
#         intPowerOfTwo *= 2
#         listOfPowersOfTwo.append(intPowerOfTwo)
#     print(listOfPowersOfTwo)
