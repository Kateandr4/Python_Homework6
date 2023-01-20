#Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
#Пример:
#Для n=4 -> [2, 2.25, 2.37, 2.44]
#Сумма 9.06

# num = int(input('Введите целое число '))
# my_list=[]
# sum1 = 0.0

# for i in range(1, num+1):
#     my_list = ((1/i)+1)**i
#     sum1 = sum1+my_list
#     print(my_list, end=", ")

# print()
# print(sum1)

from functools import reduce

num = int(input('Введите целое число '))
my_list = [((1/x)+1)**x for x in range(num+1) if x>0 ]
print(my_list)
sum1 = reduce(lambda x, y: x+y, my_list)
print(sum1)