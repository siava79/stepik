# print('Я', 'учусь', 'программировать', 'на', 'Python!')   # то, что внутри скобок команда, называется его аргументами
#
# print('Какой хороший день!')
# print()
# print('Работать мне не лень!')
# print("Здравствуй, мир!")
# print("4", "8", "15", "16", "23", "42")
#
# print(4)
# print(8)
# print(15)
# print(16)
# print(23)
# print(42)
#
# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')
# print('******')
# print('*******')
#
# name = input('Как тебя зовут?')
# print("Hi", name)
#
# a = '10'
# b = '20'
# c = '30'
import math
# print('I', 'like', 'Python', sep='***')
#
# name = input()
# print('Привет,', name, end="!")

# sep_name = input()
# a = input()
# b = input()
# c = input()
# print(a, b, c, sep=sep_name)

# a = int(input())
# b = a + 1
# c = b + 1
# print(a)
# print(b)
# print(c)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a + b + c)

# a = int(input())
# b = int(input())
# print(3 * ())
# print("Плщадь полной поверхности = ", s)
#
# a = int(input())
# b = int(input())
# c = a + b
# print(3 * (c * c * c) + 275 * (b * b) - (127 * a) - 41)

# a = int(input())
# b = a + 1
# c = a - 1
# print("Следующее за числом", a, "число:", b)
# print("Для числа", a, "предыдущее число:", c)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(3 * (a + b + c + d))

# a = int(input())
# b = int(input())
# c = a + b
# d = a - b
# e = a * b
# print(a, '+', b, '=', c)
# print(a, '-', b, '=', d)
# print(a, '*', b, '=', e)

# a = int(input())
# d = int(input())
# n = int(input())
# b = a + d * (n - 1)
# print(b)

# a = int(input())
# print(a, 2 * a, 3 * a, 4 * a, 5 * a, sep='---')

# print(2 ** 0)
# print(2 ** 1)
# print(2 ** 2)
# print(2 ** 3)
# print(2 ** (-1))
# print(2 ** 2 ** 3)
# print(9 // 12)
# print(9 % 12)
# print(12 % 9)
# print(123 // 10)
# print(82 // 2)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a * 1 * b ** (c - 1))

# a = int(input())
# print(a // 100)

# a = int(input())
# print((- a // 2) // - 1)

# a = int(input())
# h = a // 60
# m = a % 60
# print(a, "мин - это", h, "час", m, "минут.")

# a = int(input())
# # m = a % 4
# # print(m)
# print((- a // 4) // - 1)

# ()	Скобки
# **	Возведение в степень
# - (унарный минус)	Унарный минус
# *, /, //, %	Умножение, деление, целочисленное деление, остаток от деления
# +, -	Сложение, вычитание

# 123456789  // 1 % 10 ---> 9                (единицы)
#
# 123456789   // 10 % 10 ---> 8               (десятки)
#
# 123456789  // 100 % 10 ---> 7               (сотни)
#
# 123456789  // 1000 % 10 ---> 6             (тысячи)
#
# 123456789  // 10000 % 10 ---> 5           (десятки тысяч)
#
# 123456789  // 100000 % 10 ---> 4         (сотни тысяч)
#
# 123456789  // 1000000 % 10 ---> 3       (миллионы)
#
# 123456789  // 10000000 % 10 ---> 2     (десятки миллионов)
#
# 123456789  // 100000000 % 10 ---> 1   (сотни миллионов)
#
#  и т. д.

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Искомое число =', last_digit * 10 + first_digit)


# num_input = int(input())
# num1 = num_input // 100 % 10
# num2 = num_input // 10 % 10
# num3 = num_input % 10
# print(num1, num2, num3, sep="")
# print(num1, num3, num2, sep="")
# print(num2, num1, num3, sep="")
# print(num2, num3, num1, sep="")
# print(num3, num1, num2, sep="")
# print(num3, num2, num1, sep="")

# num_input = int(input())
# num1 = num_input // 1000 % 10
# num2 = num_input // 100 % 10
# num3 = num_input // 10 % 10
# num4 = num_input % 10
# print("Цифра в позиции тысяч равна", num1)
# print("Цифра в позиции cотен равна", num2)
# print("Цифра в позиции десятков равна", num3)
# print("Цифра в позиции единиц равна", num4)

# print('*****************')
# print('*', '*', sep='               ')
# print('*', '*', sep='               ')
# print('*****************')

# a = int(input())
# b = int(input())
# c = a + b
# print("Квадрат суммы", a, "и", b, "равен", (a + b) * c)
# print("Сумма квадратов", a, "и", b, "равен", (a * a) + (b * 2))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# result = (a ** b) + (c ** d)
# print(result)

# pass_one = input()
# pass_two = input()
# if pass_one == pass_two:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# num = int(input())
# if num % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# num = int(input())
# num4 = num % 10
# num3 = num // 10 % 10
# num2 = num // 100 % 10
# num1 = num // 1000 % 10
# if (num4 + num1) == (num2 - num3):
#     print("ДА")
# else:
#     print("НЕТ")

# age = int(input())
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if (num2 - num1) == (num3 - num2):
#     print("YES")
# else:
#     print("NO")

# num1 = int(input())
# num2 = int(input())
# if num1 < num2:
#     print(num1)
# else:
#     print(num2)

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# min12 = 0
# min34 = 0
# min_sum = 0
# if num1 < num2:
#     min12 = num1
# if num2 < num1:
#     min12 = num2
# if num1 == num2:
#     min12 = num1
# if num3 < num4:
#     min34 = num3
# if num4 < num3:
#     min34 = num4
# if num3 == num4:
#     min34 = num3
# if min12 < min34:
#     min_sum = min12
# if min34 < min12:
#     min_sum = min34
# if min12 == min34:
#     min_sum = min12
# print(min_sum)

# age = int(input())
# if age <= 13:
#     print("детство")
# elif age == 14:
#     print("молодость")
# elif age <= 24:
#     print("молодость")
# elif age == 25:
#     print("зрелость")
# elif age <= 59:
#     print("зрелость")
# elif age == 60:
#     print("старость")
# elif age > 60:
#     print("старость")

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# sum = 0
# if num1 > 0:
#     num1 = num1
# else:
#     num1 = 0
# if num2 > 0:
#     num2 = num2
# else:
#     num2 = 0
# if num3 > 0:
#     num3 = num3
# else:
#     num3 = 0
# print(num1 + num2 + num3)

# x = int(input())
# if (-29 <= x <= -2 ) or (8 <= x <= 25):
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# x = int(input())
# if (9999 >= x > 999) and (x % 7 == 0) or (x % 17 == 0):
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("YES")
# else:
#     print("NO")

# x = int(input())
# if (x % 4 ==0 and x % 100 != 0) or (x % 400 == 0):
#   print("YES")
# else:
#   print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 ==y2:
#     print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 == x2 or x1 == x2 + 1 or x1 == x2 - 1) and (y1 == y2 or y1 == y2 + 1 or y1 == y2 - 1):
#     print("YES")
# else:
#     print("NO")

# grade = int(input('Введите вашу отметку: '))
#
# if grade >= 90:
#     print(5)
# elif grade >= 95:
#     print(4)
# elif grade >= 70:
#     print(3)
# elif grade >= 60:
#     print(2)
# else:
#     print(1)


# a, b, c = int(input()), int(input()), int(input())
#
# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(2)
# else:
#     if a == c:
#         print(2)
#     else:
#         if b == c:
#             print(2)
#         else:
#             print(0)


# n = int(input())
# k = int(input())
# if k > n:
#     print("YES")
# elif n > k:
#     print("NO")
# else:
#     print("Don't know")


# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print("Равносторонний")
# elif  a == b < c or a == b > c or b == c > a or b == c < a or a == c > b or a == c < b:
#     print("Равнобедренный")
# elif a != b != c:
#     print("Разносторонний")


# a = int(input())
# b = int(input())
# c = int(input())
# if a < b and b < c:
#     print(b)
# elif  a < b and b > c:
#     print(c)
# elif a > b and b < c:
#     print(a)
# elif a < b and b > c:
#     print(a)
# elif a > b and b < c:
#     print(c)
# elif a > b and b > c:
#     print(b)

# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print("31")
# elif a == 2:
#     print("28")
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print("30")

# a = int(input())
# if a <= 59:
#     print("Легкий вес")
# elif a == 60 or a <= 63:
#     print("Полусредний вес")
# elif a == 64 or a <= 68:
#     print("Полусредний вес")

# a = int(input())
# b = int(input())
# c = str(input())
# if c == "/" and b == 0:
#     print("На ноль делить нельзя!")
# elif c == "/":
#     print(a / b)
# elif c == "*":
#     print(a * b)
# elif c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# else:
#     print("Неверная операция!")

# a = input().lower()
# b = input().lower()
#
# # Только основные цвета для проверки
# allowed_colors = {"красный", "синий", "желтый"}
#
# # Проверка на валидность цветов
# if a not in allowed_colors or b not in allowed_colors:
#     print("ошибка цвета")
# elif a == b:
#     print(a)
# elif (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
#     print("фиолетовый")
# elif (a == "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
#     print("оранжевый")
# elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
#     print("зелёный")
# if a not in allowed_colors or b not in allowed_colors:
#     print("ошибка цвета")
# elif a == b:
#     print(a)
# else:
#     print("ошибка цвета")

# a = int(input())
#
# if a == 0:
#     print("зеленый")
# elif a > 0 and a <= 10:
#     if a % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif a > 0 and a <= 18:
#     if a % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# elif a > 0 and a <= 28:
#     if a % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif a > 0 and a <= 36:
#     if a % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# else:
#     print("ошибка ввода")


# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# if a2 > b1 or a1 > b2:
#     print("Пустое множество")
# elif b1 == a2:
#     print(b1)
# elif a1 == b2:
#     print(a1)
# elif a1 < a2 < b1 < b2:
#     print(a2, b1)
# elif a2 < a1 < b2 < b1:
#     print(a1, b2)
# elif a1 == a2 and b1 < b2:
#     print(a1, b1)
# elif a1 == a2 and b2 < b1:
#     print(a1, b2)
# elif a2 < a1 < b1 < b2:
#     print(a1, b1)
# elif a1 < a2 < b2 < b1:
#     print(a2, b2)
# elif a2 < a1 and b1 == b2:
#     print(a1, b1)
# elif a1 < a2 and b1 == b2:
#     print(a2, b2)
# elif a1 == a2 and b1 == b2:
#     print(a1, b1)

# a = int(input())
# if a % 100 == 0:
#     print("YES")
# else:
#     print("NO")

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# x1y1 = x1 + y1
# x2y2 = x2 + y2
# if x1y1 % 2 == 0 and x2y2 % 2 == 0:
#     print("YES")
# elif x1y1 % 2 != 0 and x2y2 % 2 != 0:
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# b = str(input())
# if (10 <= a <= 15) and (b == 'f' and b != 'm'):
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# if a == 1:
#     print("I")
# elif a == 2:
#     print("II")
# elif a == 3:
#     print("III")
# elif a == 4:
#     print("IV")
# elif a == 5:
#     print("V")
# elif a == 6:
#     print("VI")
# elif a == 7:
#     print("VII")
# elif a == 8:
#     print("VIII")
# elif a == 9:
#     print("IX")
# elif a == 10:
#     print("X")
# else:
#     print("ошибка")

# a = int(input())
# if a % 2 != 0:
#     print("YES")
# elif a % 2 == 0 and 2 <= a <= 5:
#     print("NO")
# elif a % 2 == 0 and 6 <= a <= 20:
#     print("YES")
# elif a % 2 == 0 and a >= 20:
#     print("NO")

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# x1y1 = x1 + y1
# x2y2 = x2 + y2
# if x1y1 % 2 == 0 and x2y2 % 2 == 0:
#     print("YES")
# elif x1y1 % 2 != 0 and x2y2 % 2 != 0:
#     print("YES")
# else:
#     print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if abs(x2 - x1) == abs(y2 - y1):
#     print("YES")
# else:
#     print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# a = x1 + y1 + x2 + y2
# if a % 2 != 0 and x1 != x2 and y1 != y2:
#     print("YES")
# else:
#     print("NO")
#
#
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if abs(x2 - x1) == abs(y2 - y1) or x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")

# a = float(input())
# b = float(input())
# s = (1 / 2) * a * b
# print(s)

# s = float(input())
# v1 = float(input())
# v2 = float(input())
# vsum = v1 + v2
# time = s / vsum
# print(time)

# a = float(input())
# if a == 0:
#     print("Обратного числа не существует")
# else:
#     x = 1 / a
#     print(x)

#
# tf = float(input())
# tc = 5 / 9 * (tf - 32)
# print(tc)

# a = float(input())
# if a <= 2:
#     print(a * 10.5)
# elif a > 2:
#     a = (a - 2) * 4 + 21
#     print(a)

# a = float(input())
# x = (a * 10) % 10
# print(x / 10)
# # y = x - x
# # print(y)

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# x = min(a, b, c, d, e)
# y = max(a, b, c, d, e)
# print("Наименьшее число = ", x)
# print("Наибольшее число = ", y)


# a, b, c = int(input()), int(input()), int(input())
# asum = a + b + c
# xmin = min(a, b, c)
# ymax = max(a, b, c)
# xysum = xmin + ymax
# average = asum - xysum
# print(ymax)
# print(average)
# print(xmin)

# a = int(input())
# x1 = a // 100 % 10
# x2 = a // 10 % 10
# x3 = a // 1 % 10
# x123 = x1 + x2 + x3
# xmin = min(x1, x2, x3)
# xmax = max(x1, x2, x3)
# xsumm = xmin + xmax
# xaverage = x123 - xsumm
# y = xmax - xmin
# if y == xaverage:
#     print("Число интересное")
# else:
#     print("Число неинтересное")


# a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
# ma = abs(a)
# mb = abs(b)
# mc = abs(c)
# md = abs(d)
# me = abs(e)
# msumm = ma + mb + mc + md + me
# print(msumm)

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x12 = abs(x2 - x1)
# y12 = abs(y2 - y1)
# d = x12 + y12
# print(d)

# name = input()
# surname = input()
# print('Hello', name, surname + '!', 'You have just delved into Python')

# team = input()
# lengthTeam = len(team)
# print('Футбольная команда', team, 'имеет длину', lengthTeam, 'символов')

# city1, city2, city3 = input(), input(), input()
# length_city1 = len(city1)
# length_city2 = len(city2)
# length_city3 = len(city3)
# city_min = min(city1, city2, city3, key=len)
# city_max = max(city1, city2, city3, key=len)
# print(city_min)
# print(city_max)

# a, b, c = input(), input(), input()
# len_a = len(a)
# len_b = len(b)
# len_c = len(c)
# summ = len_a + len_b + len_c
# min_number = min(len_a, len_b, len_c)
# max_number = max(len_a, len_b, len_c)
# min_max_summ = min_number + max_number
# average_number = summ - min_max_summ
# ab = average_number - min_number
# bc = max_number - average_number
# if ab == bc:
#     print("YES")
# else:
#     print("NO")

# language1 = 'JavaScript'
# language2 = 'Java'
#
# print(language1 in language2)
# print(language2 in language1)

# s = '1'
# if s in 'abc123abc':
#     print('YES')
# else:
#     print('NO')

# email = input()
# if '@' in email and '.' in email:
#     print("YES")
# else:
#     print("NO")

# from math import *
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# p = sqrt((x1 - x2)**2 + (y1 - y2)**2)
# print(p)

# from math import pi
# R = float(input())
# S = pi * (R ** 2)
# C = (2 * pi) * R
# print(S)
# print(C)

# from math import *
# a, b = float(input()), float(input())
# av = (a + b) / 2
# ge = sqrt(a * b)
# ga = 2 * (a * b) / (a + b)
# kv = sqrt((a ** 2 + b ** 2) / 2)
# print(av)
# print(ge)
# print(ga)
# print(kv)

# from math import *
# x = float(input())
# r = (x * pi) / 180
# result = sin(r) + cos(r) + tan(r) ** 2
# print(result)

# from math import *
# b = float(input())
# f = floor(b)
# c = ceil(b)
# x = f + c
# print(x)

# from math import *
# a, b, c = float(input()), float(input()), float(input())
# D = b**2 - 4*a*c
# if D > 0:
#     # Два различных вещественных корня
#     x1 = (-b - sqrt(D)) / (2 * a)
#     x2 = (-b + sqrt(D)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))
# elif D == 0:
#     # Один вещественный корень
#     x = -b / (2 * a)
#     print(x)
# else:
#     # Нет вещественных корней
#     print("Нет корней")

# from math import *
# n, a = int(input()), float(input())
# s = n * (a ** 2) / 4 / tan(pi / n)
# print(s)

# for i in range(10):
#     num = int(input())
#     print("Квадрат вашего числа равен:", num * num)
#
# print("Цикл завершен")

# a = input()
# b = int(input())
# for i in range(b):
#     print(a)

# for i in range(6):
#     print("AAA")
# for i in range(5):
#     print("BBB")
# print("E")
# for i in range(9):
#     print("TTTTT")
# print("G")

# b = int(input())
# for i in range(b):
#      print("*******************")

# n = int(input())
# for i in range(n):
#     print("*" * (n - i))

# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(n):
#     print(i + 1, m)
#     m = (m + (m / 100) * p)

# for i in range(100, 1000):  # перебираем числа от 100 до 999
#     if i % 10 == 5:         # используем остаток от деления на 10, для получения последней цифры
#         print(i)

# m = int(input())
# n = int(input())
# n = n + 1
# for i in range(m, n):
#     print(i)

# m = int(input())
# n = int(input())
# if m < n:
#     n = n + 1
#     for i in range(m, n):
#         print(i)
# elif m > n:
#     n = n - 1
#     for i in range(m, n, -1):
#         print(i)
# elif m == n:
#     print(m)

# m = int(input())
# n = int(input())
# if n % 2 != 0:
#     n = n - 1
# for i in range(m, n, -1):
#     if i % 2 != 0:
#         print(i)

# m = int(input())
# n = int(input())
# if n % 2 != 0:
#     n = n - 1
# for i in range(m, n, -1):
#     if i % 2 != 0:
#         print(i)

# m = int(input())
# n = int(input())
# for i in range(m, n+1):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)

# n = int(input())
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)

# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
#
# print('Было введено', counter, 'чисел, больших 10.')

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1

# print(counter)

# total = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
#
# print('Сумма чисел больших 10 равна',  total)

# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# largest = 0
# for _ in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
#
# print('Наибольшее число равно', largest)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# num1 = int(input())
# num2 = int(input())
# total = 0
# for i in range(num1, num2+1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         total += 1
#
# print(total)


# total = 0
# n = int(input())
# for i in range(n):
#     a = int(input())
#     total += a
#
# print(total)

# from math import *
# total = 0
# n = int(input())
# # for i in range(n):
# #     a =
# #     total += a
# #
# # print(total)

# n = int(input())
# total = 0
# for i in range(1, n+1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         total += i
#
# print(total)

# n = int(input())
# factorial = 1
# for i in range(2, n+1):
#     factorial *= i
#
# print(factorial)


# summ = 1
# for i in range(1, 11):
#     a = int(input())
#     if a != 0:
#         summ *= a
#
# print(summ)

# max1 = 0
# max2 = 0
# n = int(input())
# for i in range(1, n+1):
#     a = int(input())
#     if a > max1:
#         max2 = max1
#         max1 = a
#     elif max1 > a > max2:
#         max2 = a
#
# print(max1)
# print(max2)

# total = 0
# for i in range(1, 11):
#     n = int(input())
#     if n % 2 == 0:
#         total += 1
#
# if total == 10:
#     print("YES")
# else:
#     print("NO")

                                                    # ЦИКЛ - WHILE

# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())

# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
#
# print(a)

# word = input()
# summ = 0
# while word != "стоп" and word != "хватит" and word != "достаточно":
#     summ += 1
#     word = input()

# print(summ)


# цикл выполняется пока введенное число делится на 7
# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())

# цикл выполняется пока на вход подается числа не ниже 0, в конце вывод суммы введенных чисел
# num = int(input())
# summ = 0
# while num >= 0:
# while num >= 0:
#     summ += num
#     num = int(input())
#
# print(summ)

# посчет цифры "5" в цикле при условии, что введенное число не меньше 1 и не более 5
# num = int(input())
# count = 0
# while 0 < num <= 5:
#     if num == 5:
#         count += 1
#     num = int(input())
#
# print(count)

# на вход подается сумма оплаты, номинал банкнот 25, 10, 5, 1. Необходимо написать прогу минимального кол-ва банктнот, которые можно использовать
# num = int(input())
# count = 0
# while num >= 25:
#     count += 1
#     num -= 25
# while 25 > num >= 10:
#     count += 1
#     num -= 10
# while 10 > num >= 5:
#     count += 1
#     num -= 5
# while 5 > num >= 1:
#     count += 1
#     num -= 1
#
# print(count)


# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа
#
# print(n)

# вводится число, дальше цикл, который берет по очереди каждое последнее число и выводит его в обратном порядке
# num = int(input())
# last_digit = 0
# while num != 0:
#     last_digit = num % 10
#     num = num // 10
#     print(last_digit)

# то же самое, только число полностью на одой строке выводится в обратном порядке
# num = int(input())
# last_digit = 0
# while num != 0:
#     last_digit = num % 10
#     num = num // 10
#
# print(last_digit, end='')


# ввод числа и определение максимального и минимального числа
# num = int(input())
# max_number = 0
# min_number = 9
# last_digit = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > max_number:
#         max_number = last_digit
#     if last_digit < min_number:
#         min_number = last_digit
#     num = num // 10
#
# print(max_number)
# print(min_number)



# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

# num = int(input())
# summ = 0
# quantity = 0
# counter = 0
# multiplication = 1
# average = 0
# original_num = num
# last_digit = num % 10
# while num != 0:
#     final_digit = num % 10
#     summ += final_digit
#     quantity += 1
#     multiplication *= final_digit
#     num = num // 10
#
# first_digit = original_num
# while first_digit >= 10:
#     first_digit //= 10
#
# average = summ / quantity
# mfl = first_digit + last_digit
#
# print(summ)
# print(quantity)
# print(multiplication)
# print(average)
# print(first_digit)
# print(mfl)


# ввод числа и вывод второго в начале числа
# last_digit = 0
# num = int(input())
# while num > 10:
#     last_digit = num % 10
#     num = num // 10
#
# print(last_digit)


# ввод числа, сравнение одинаковые ли все числа или нет
# num = int(input())
# max_number = 0
# min_number = 9
# last_digit = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > max_number:
#         max_number = last_digit
#     if last_digit < min_number:
#         min_number = last_digit
#     num = num // 10
#
# if max_number == min_number:
#     print("YES")
# else:
#     print("NO")


# программа, проверяющая введенную цифру, должна вывести "YES", если каждая следующая цифра слева направо больше предыдущей
# num = int(input())
# flag = True
# while num > 9:
#     if num % 10 <= (num // 10) % 10:
#         flag = True
#     else:
#         flag = False
#         break
#     num = num // 10
#
# if flag:
#     print("YES")
# else:
#     print("NO")



# пример использования оператора "continue"
# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)


# найти наименьший делитель введенного числа
# n = int(input())
# min_n = 0
# for i in range(2, n+1):
#     if n % i != 0:
#         continue
#     if n % i == 0:
#         break
#
# print(i)

# ввод числа и вывод определенных
# n = int(input())
# for i in range(1, n+1):
#     if 5 <= i <= 9:
#         continue
#     elif 17 <= i <= 37:
#         continue
#     elif 78 <= i <= 87:
#         continue
#     else:
#         print(i)


# else в блоке циклов WHILE

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Цикл завершен.')


# n = 5
# while n > 0:
#     n -= 1
#     print(n)
#     if n == 2:
#         break
# else:
#     print('Цикл завершен.')

# n = 0
# while n < 10:
#     n += 2
#     print(n)
# else:
#     print('Цикл завершен.')




# count = 0
# n = 0
# factorial = 1
# for i in range(1, 11):
#     n = int(input())
#     if n >= 0:
#         count = count + 1
#         factorial *= n

# if count > 0:
#     print(count)
#     print(factorial)
# else:
#     print('NO')


# ввод 10 чисел и полсчет суммы всех отрицательных чисел и максимального отрицательного
# summ = 0
# n_loss = 0
# for i in range(1, 11):
#     n = int(input())
#     if n < 0:
#         summ += n
#         if n > n_loss or n_loss == 0:
#             n_loss = n
#
# if summ < 0:
#     print(summ)
#     print(n_loss)
# else:
#     print("NO")



# ввод 7 чисел и вывод суммы чисел кратных двух
# summ = 0
# n = 0
# for i in range(1, 8):
#     n = int(input())
#     if n % 2 == 0:
#         summ += n
# if summ > 0:
#     print(summ)
# else:
#     print("0")


# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit == 0:
#         max_digit = digit
#     elif digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
#
# if max_digit >= 0:
#     print(max_digit)
# else:
#     print('NO')


# ввод числа и произведение всех цифр числа
# n = int(input())
# factorial = 1
# while n > 0:
#     digit = n % 10
#     factorial = factorial * digit
#     n //= 10
# print(factorial)


# пример вложенного цикла с оператором "break"
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             break
#         print(i, j)


# пример вложенного цикла с оператором "continue"
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i, j)


# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')


# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
#
# print(counter)


# n = int(input())
# x = 0
# for i in range(n):
#     x += 1
#     for j in range(5):
#         print(x, end=' ')
#     print()


# n = int(input())
# for i in range(n):
#     i += 1
#     for j in range(1, 10):
#         summ = i + j
#         print(i, "+", j, "=", summ)
#     print()



# вывод равнобедренного треугольника с помощью знака "*"
# n = int(input())
# x = n // 2
# for i in range(x):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(1):
#     for j in range(x + 1):
#         print('*', end='')
#     print()
# for i in range(x):
#     for j in range(x - i):
#         print('*', end='')
#     print()



# n = int(input())
# x = 0
# for i in range(n):
#     x += 1
#     for j in range(i + 1):
#         print(x, end='')
#     print()

# шаблон решения уравнения с использованием вложенных циклов
# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)





# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка –
# 10 рублей, за корову –
# 5 рублей, за телёнка –
# 0.5 рубля и надо купить
# 100 голов скота?
# Примечание. Используйте вложенный цикл for.

# total = 0
# for b in range(0, 11):
#     for k in range(0, 21):
#         for t in range(0, 201):
#             if b + k + t == 100 and 10 * b + 5 * k + 0.5 * t == 100:
#                 total += 1
#                 print('b =', b, 'k =', k, 't =', t)
# print('Общее количество натуральных решений =', total)



# Дано натуральное число
# n. Напишите программу, которая печатает численный треугольник с высотой, равной
# n, в соответствии с примером:
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ------------------------------------
# n = int(input())
# x = 0
# for i in range(n):
#     for j in range(i + 1):
#         x += 1
#         print(x, end=' ')
#     print()

# for i in range(20, 10, -2):
#     print('Привет', i)




# Дано натуральное число
# n
# n. Напишите программу, которая печатает численный треугольник с высотой, равной
# n
# n, в соответствии с примером:
#
# 1
# 121
# 12321
# 1234321
# 123454321

# n = int(input())
# for i in range(1, n+1):
#      for j in range(1, i + 1):
#          print(j, end='')
#      for j in range(i-1, 0, - 1):
#          print(j, end='')
#      print()


# На вход программе подаются два натуральных числа
# a< b). Напишите программу, которая находит натуральное число из отрезка
# [a;b] (от a до b включительно) с максимальной суммой делителей. Если чисел
# с максимальной суммой делителей несколько, то искомым числом является наибольшее из них.
#  Ваша программа должна выводить ответ в следующем формате:
#
# <число с максимальной суммой делителей> <сумма делителей этого числа>

# n = int(input())
# m = int(input())
# max_count = 0
# number = 0
# total_j = 0
# count = 0
# for i in range(n, m+1):
#     count = max_count
#     total_j = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             total_j += j
#     if total_j >= count:
#         max_count = total_j
#         number = i
#     else:
#         max_count = count
# print(number, max_count, sep=' ')





cars = [
    {"brand": "BMW", "model": "X5", "year": 2005, "max_speed": 240, "price": 1368515},
    {"brand": "BMW", "model": "X3", "year": 2017, "max_speed": 260, "price": 1798913},
    {"brand": "Mersedes", "model": "A-Class", "year": 2022, "max_speed": 300, "price": 1798913},
    {"brand": "Hyuinday", "model": "Accent", "year": 2017, "max_speed": 240, "price": 1698913}
]

# for car in cars:
#     print(f"Бренд: {car['brand']}, Модель: {car['model']}, Год выпуска: {car['year']}, Максимальная скорость: {car['max_speed']}, Средняя стоимость: {car['price']} грн.")
#
# for car in cars:
#     print(f"Бренд: {car['brand']}, Модель: {car['model']}, Год выпуска: {car['year']}")
#
for car in cars:
    if car["max_speed"] > 240:
        print(f"Бренд: {car['brand']}, Модель: {car['model']}, Год выпуска: {car['year']}")


for i in range(len(cars)):
    if cars[i] ['max_speed'] > 200 and cars[i] ['brand'] == "BMW":
        print(f"Бренд: {cars[i] ['brand']}, Модель: {cars[i]['model']}")








