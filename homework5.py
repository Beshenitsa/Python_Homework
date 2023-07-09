# Task 1. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# A = int(input('Input number A, please: '))
# B = int(input('Input number B, please: '))

# def Exponentiation(A, B):
#     if B == 0:
#         return 1
#     else:
#         return A * Exponentiation(A, B - 1)

# print(Exponentiation(A, B))


# Task 2. Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# A = int(input('Input number A, please: '))
# B = int(input('Input number B, please: '))

# def Sum (A, B):
#     if B == 0:
#         return A
#     return 1 + Sum(A, B - 1)

# print(Sum(A, B))