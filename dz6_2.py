#Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на позиции с нечетным индексом.

# my_list = [2, 3, 5, 9, 3, 5]

# print(my_list)
# sum = 0

# for i in range(len(my_list)):
#      if i % 2 !=0:
#          sum=sum+my_list[i]
# print(f'сумма нечетных элементов = {sum}')

#--------------

my_list = [2, 3, 5, 9, 3, 5]
print(my_list)
sum = 0

for i, item in enumerate(my_list):
   if i % 2 !=0:
    sum=sum+my_list[i]
print(f'сумма нечетных элементов = {sum}')