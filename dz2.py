#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

#num = input('Введите число: ')
#sum = 0
#for a in num:
 #   if a.isdigit():
  #      sum += int(a)

#print(f"Сумма {num} равна: ", sum)

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#*Пример:*
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


#N = int(input('Введите число '))

#fact = 1
#for i in range(N):
   #fact = 1
#for i in range(N):
 #   i = i + 1
 #   fact = i * fact
  #  print(fact, end=" ") 

#Задайте список из n чисел последовательности (1+1/n)^n  и выведите на экран их сумму.
#*Пример:*
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
		 
 
#n = int(input('Введите число: '))
 	 
#def get_squer(n):
 #	return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
#nums = get_squer(n)
#print(nums)
#print(round(sum(nums), 5))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 

#from random import randint
#numbers = []
#for i in range(5):
#    numbers.append(randint (-10,10))
#print(numbers)
#x = int(input('Введите позицию первого элемента: '))
#y = int(input('Введите позицию второго элемента: '))
#for i in range(len(numbers)):
 #   mult = numbers[x]*numbers[y]
#print(f'Произведение: {numbers[x]} * {numbers[y]} =', mult)

 #Реализуйте алгоритм перемешивания списка.
#import random
#test_list = [1, 4, 5, 6, 3]
#print ("Исходный список : " + str(test_list))
#for i in range(len(test_list)-1, 0, -1):
 #	  j = random.randint(0, i + 1) 
#test_list[i], test_list[j] = test_list[j], test_list[i]  
#print ("Перемешанный список : " +  str(test_list))

# 2 вариант
#import random
#test_list = [1, 4, 5, 6, 3]
#print ("Исходный список : " + str(test_list))
#random.shuffle(test_list)
#print ("Перемешанный : " +  str(test_list))
