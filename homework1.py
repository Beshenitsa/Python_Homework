# Task 1: Найдите сумму цифр трехзначного числа.

# num = int(input("Input three-digit number, please: "))

# if num > 99 and num < 1000:
#     sum = 0
#     while num > 0:
#         x = num % 10
#         sum = sum + x
#         num = num // 10
#         print(sum)
# else:
#     print("Sorry, your number is not three-digit.")

# Task 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# sum = int(input("Input he amount of jouravliks, please: "))

# if sum >= 6 and 0 == sum % 6:
#     child1 = sum // 6
#     child2 = child1
#     child3 = (child1 + child2) * 2
#     print(child1, child2, child3)
# elif sum < 6:
#     print("Nope. I know they made more than that, try again.")
# else: 
#     print("It seems like one of jouravliks left unfinished.")

# Task 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# ticketNumber = list(input("Input the six-digit number of your ticket, please: "))

# if len(ticketNumber) < 6:
#     print("One or more digits are missing. Please, try again.")
# elif len(ticketNumber) > 6:
#     print("You have input way too many digits. Please, try again.")
# elif len(ticketNumber) == 6:
#     firstSum = int(ticketNumber[0]) + int(ticketNumber[1]) + int(ticketNumber[2])
#     secondSum = int(ticketNumber[3]) + int(ticketNumber[4]) + int(ticketNumber[5])
#     if firstSum == secondSum:
#         print("You've got a lucky ticket!")
# else:
#     print("This is a regular ticket, but don't be upset, maybe next time.")

# Task 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# lenght = int(input("Inpur the length of the chocolate in chocolate slices, please: "))
# width = int(input("Input the width of the chocolate in chocolate slices, please: "))
# quantity = int(input("Input the amount of slices you would like to break off: "))

# square = lenght * width
# if quantity > square:
#     input("The piece you want to break off is bigger than a piece of chocolate you've got.")
# elif quantity < square:
#     if ((quantity % lenght == 0) or (quantity % width == 0)):
#         input("Yes, you can break it off with just one line.")
# else:
#     input("No, you cannot break if off with just one line.")
