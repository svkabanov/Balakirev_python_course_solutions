# import math
# a, b = map(int, input().split())
# print(round(math.sqrt(a**2+b**2),2))

# import math
# n, m = map(int, input().split())
# print(math.ceil((n+m)/20))
#
# x = int(input())
# print(int(500/(x*0.9)))

# a = 7
# b = -4
# c = 3
# print(a,b,c,sep='\n')

# s1 = "Hello"
# s2 = "Balakirev"
# print(s1,end=' ')
# print(s2)

# s1, s2 = map(str.strip, input().split())
# print(f'Word 1: {s1} | Word 2: {s2}')

# a,b = map(int,input('Введите два цеоых числа через пробел:').split())
# print(a**b)

# a,b = map(float,input().split())
# print(a+b)

# X, Y = map(int, input().split())
# print(int(X+X*2+Y+Y*4))
#
# a=float(input())
# b=float(input())
# print(2*(a+b))

# import math
# print(round(math.pi,3))

# x=float(input())
# print(f'Вы ввели число {x}')

# x=7
# print(not (x % 2==0 and x % 3 ==0))

# x=round(float(input()),2)
# print((x-int(x))*100 > 50)

# a, b, c = map(int, input().split())
# print((a+b > c) and (a+c>b) and (b+c > a))

# x=float(input())
# print((0<=x<=2) or (10 <= x <= 20))

# s1, s2 = input().split()
# print(str(s1 in s2), str(s1 ==s2), str(s1 > s2),str(s1 < s2),sep=' ')

# s1, s2 = input().split()
# print(f'Коды: {s1} = {ord(s1)}, {s2} = {ord(s2)}')

# s=input()
# print(s[0]+s[-1])

# s1=input()
# s2=input()
# print(s1[0::2], s2[1::2])

# s=input()
# s2=s[0:5]
# print(s2[::-1])

# s1,s2 = input().split()
# print(s1[:len(s2)][1::2] == s2[1::2])

# s=input()
# print(s[:1].upper()+s[1:].lower())

# s=input()
# print(s.count('-'))

# s=input()
# print(s.find('ra'))

# s=input()
# print(s.replace('---','-').replace('--','-'))

# s=input().split()
# for i in s:
#     print(i.rjust(3,'0'))

# s=input().split()
# print(len(s))


# print(';'.join(input().split()))

# s1,s2 = input().split()
# print(s1+'\\'+s2)

# s=input()
# s=s.replace(' ','\'',1)
# s=s.replace(' ', '\"')
# print(s)

# s=input()
# print('\"' + s + '\"')

# name = input()
# surname = input()
# age=int(input())
# print('Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!'.format(name, surname, age))

# width, depth, height = map(int,input().split())
# print(f'Габариты: {width} x {depth} x {height}')

# a, b = map(int,input().split())
# print(f'{min(a,b)} {max(a,b)}')
# print(type(map(int,input().split())))

# city=input()
# street=input()
# house_number = input()
# flat_number = input()
# print(f'г. {city}, ул. {street}, д. {house_number}, кв. <номер квартиры>')

# dollar_rate = float(input())
# rouble_number = int(input())
# print(f'Вы можете получить {int(rouble_number//dollar_rate)}$ за {rouble_number} рублей по курсу {dollar_rate}')

# lst=list(map(int,input().split()))
# # lst=map(int,input().split())
# print(lst)

# cities = input().split()
# print(cities)
# print('Москва' in cities)

# cities = input().split()
# print(cities[len(cities)-1])

# marks = list(map(int, input().split()))
# print(f'{sum(marks)/len(marks):.1f}')

# title =input()
# author=input()
# page_number = int(input())
# price = float(input())
# lst=[title,author,page_number,price]
# del lst[2]
# lst[1]="Пушкин"
# lst[2]*=2
# print(lst)

# lst=list(map(int,input().split()))
# print(max(lst),min(lst),sum(lst), sep = ' ')

# lst=list(map(int,input().split()))
# lst = sorted(lst,reverse=True)
# print(*lst)

# lst = input().split()
# cities = ["Москва", "Тверь", "Вологда"]
# lst = lst + cities
# print(*lst)

# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[-4:])

# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[1::2])

# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[::-2])

# lst=list(map(int,input().split()))
# lst.append(lst[0] != lst[-1])
# print(*lst)

# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1,'Ульяновск')
# print(*cities)

# lst=list(input())
# # print(lst)
# lst.pop(0)
# lst[lst.index('7')]='8'
# lst=list("".join(lst).split(sep='-'))
# print("".join(lst))

# lst=input().split()
# print(lst[2] + ' ' + lst[0][0] + '.' + lst[1][0] + '.')

# lst=list(map(int,input().split()))
# lst.sort()
# lst=list(map(str,lst))
# # print(lst[0:3])
# print(' '.join(lst[0:3]))

# lst=list(map(int,input().split()))
# lst.sort()
# # print(*lst[0:3])
# print(lst[0],lst[1],lst[2])

# lst=list(map(int,input().split()))
# lst.append(lst.pop() % 2 != 0)
# print(*lst)

# lst=list(map(int,input().split()))
# print(lst.count(2))

# lst = input().split()
# # print(lst)
# lst.sort()
# lst.pop(0)
# print(*lst)

# lst = [5.4, 6.7, 10.4]
# digs=list(map(int,input().split()))
# lst.append(digs)
# print(lst)

# lst=[]
# lst.append(input().split())
# lst.append(input().split())
# lst.append(input().split())
# print(lst)
#
# lst=[]
# lst.append(list(map(int,input().split())))
# lst.append(list(map(int,input().split())))
# lst.append(list(map(int,input().split())))
# print(lst[0][3],lst[1][3],lst[2][3])

# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#     ["Я", "Python", "выучил", "с", "каналом"],
#     ["Балакирев", "что", "раздавал?"]]
# # world = input()
# # print((world in t[0]) or (world in t[1]) or (world in t[2]))
# # print((world in t[2]))
# print(t)
# print(str(t))
# # world = input()
# # print((world in str(t)))
# print(sum(t, []))

# a,b = map(float,input().split())
# if a > b:
#     print(a)
# else:
#     print(b)

# world=input()
# world=world.lower()
# # print(world)
# lst=list(world)
# lst_reverse=lst[::-1]
# # print(lst_reverse)
# # print(lst.reverse())
# # print(lst)
# if lst == lst_reverse:
#     print('ДА')
# else:
#     print('НЕТ')

# m,n = map(int,input().split())
# if m % n == 0:
#     print(int(m/n))
# else:
#     print(f'{m} на {n} нацело не делится')

# a, b, c = map(int,input().split())
# if c**2 == a**2 + b**2:
#     print('ДА')
# else:
#     print('НЕТ')

# a = list(input())
# if int(a[-1]) == 7:
#     print('ДА')
# else:
#     print('НЕТ')

# world=input()
# # print(world.count('t'))
# if world.count('t') and world.count('h') and world.count('o'):
#     print('ДА')
# else:
#     print('НЕТ')

# cities = input().split()
# if 'Москва' in cities:
#     cities.remove('Москва')

# a, b, c, d = map(int,input().split())
# if (a - c > 1 and b - d > 1) or (a - d > 1 and b - c > 1):
#     print('ДА')
# else:
#     print('НЕТ')

# number = list(map(int,list(input())))
# if sum(number[:3]) == sum(number[3:]):
#     print('ДА')
# else:
#     print('НЕТ')

# t = float(input())
# if 0 <= t % 5 <= 3:
#     print('green')
# else:
#     print('red')

# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# m=m.split(sep='\n')
# # print(m)
# i = int(input())
# if i<1:
#     print('Введите число от 1 до 6')
# elif i >6:
#     print('Введите число от 1 до 6')
# else:
#     print(m[i-1])

# a, b, c = map(int,input().split())
# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b < c:
#         print(b)
#     else:
#         print(c)

# weight = float(input())
# if weight <= 60:
#     print(1)
# elif 60 < weight <= 64:
#     print(2)
# elif 64 < weight <= 69:
#     print(3)
# else:
#     print(4)

# days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# n = int(input())
# print(days[n-1])

# n = int(input())
# days =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if n < 1:
#     print('Введите правльный месяц')
# elif n > 12:
#     print('Введите правльный месяц')
# else:
#     print(days[n-1])

# m, n = map(int,input().split())
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if n == 1:
#     print(f'{m - 1:02}.{days[m - 2]} {m:02}.{n + 1:02}')
#     # print(f'{str(m-1).rjust(2,'0')}.{str(days[m-2]).rjust(2,'0')} {str(m).rjust(2,'0')}.{str(n+1).rjust(2,'0')}')
# elif n == days[m-1]:
#     print(f'{str(m).rjust(2,'0')}.{str(n-1).rjust(2,'0')} {str(m+1).rjust(2,'0')}.{str(1).rjust(2,'0')}')
# else:
#     print(f'{str(m).rjust(2, '0')}.{str(n - 1).rjust(2, '0')} {str(m).rjust(2, '0')}.{str(n+1).rjust(2, '0')}')

# k = int(input())
# days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# print(days[k % 7 -1])

# a = float(input())
# b = float(input())
# d = a if a > b else b
# print(d)

# a = int(input())
# print(('' if a % 3 == 0 else 'не ') + 'кратно 3')

# w= list(input().lower())
# reversed_w = w[::-1]
# print(('' if w == reversed_w else 'не ') + 'палиндром')
# print(w)
# print(reversed_w)

# k = int(input())
# print( True if k ==1 else False)

# k = int(input())
# print( 0 if k ==59 else k+1 )

# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# a, b, c = map(int,input().split())
# print(('#' if (m[a-1] == 'до' or m[a-1] == 'фа') else '' ) + m[a-1] +
#       ' ' + ('#' if (m[b-1] == 'до' or m[b-1] == 'фа') else '' ) + m[b-1] +
#       ' ' +('#' if (m[c-1] == 'до' or m[c-1] == 'фа') else '' ) + m[c-1]  )

# n, m = map(int, input().split())
# while n <= m:
#     print(n**2, end = ' ')
#     n+=1

# price = float(input())
# i = 2
# while i <= 10:
#     print(f'{i*price:.1f}', end=' ')
#     i +=1

# n = int(input())
# s = 0
# i = 1
# while i < n+1:
#     s += 1/i
#     i += 1
#
# print(f'{s:.3f}')

# s, i = 0, 1
# while i != 0:
#     i = int(input())
#     s += i
#
# print(s)

# str = input()
# while '--' in str:
#     str = str.replace('--', '-')
# print(str)

# number = list(input())
# product = 1
# l = len(number)
# i=0
# while i < l:
#     product *= int(number[i])
#     i += 1
#
# print(product)

# n = int(input())
# lst = [1, 1]
# l = 2
# while l < n :
#     lst.append(lst[l-1] + lst[l-2])
#     l += 1
# print(*lst)

# n = int(input()) -3
# am = 1
# while n >= 0:
#     am *= 2
#     n -= 3
#
# print(am)

# n = int(input())
# s = 1000
# while n:
#     s *= 1.05
#     n -= 1
# print(f'{round(s,2)}')

# n, m = map(int, input().split())
#
# while n <= m:
#     if n % 2 != 0:
#         print(n,end = ' ')
#     n += 1

# i = 100
# while i <= 999:
#     if i % 47 == 43 and i % 3 == 0:
#         print(i,end = ' ')

# p = [0] * 10
# while sum(p) < 5:
#     i = int(input())
#     if p[i-1] == 1:
#         continue
#     p[i-1]=1
#
# print(*p)

# product = 1
# n = 1
# while n != 0:
#     n = int(input())
#     if n <= 0:
#         continue
#     product *= n
#
# print(product)

# flag = 'ДА'
# lst = input().split()
# while lst:
#     if len(lst.pop()) <= 5:
#         flag = 'НЕТ'
#         break
#
# print(flag)

# flag = 'НЕТ'
# lst = input().lower().split()
# while lst:
#     name = lst.pop()
#     if name[0] == name[-1]:
#         flag = 'ДА'
#         break
#
# print(flag)

# n = int(input())
# i = 1
# if n > 99:
#     print('слишком большое значение n')
#     i = n +1
#
# while i < n+1:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, end = ' ')
#         i +=5
#
#     i += 1

# n = int(input())
# i = 1
# while i**2 <= n:
#     i += 1
# print(i)

# x = int(input())
# start = 10
# days = 1
# while start <= x:
#     start *= 1.1
#     days += 1
#
# print(days)

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# l = len(lst_in)
# i = 0
# while i < l:
#     if len(lst_in[i].split()) != 1:
#         del lst_in[i]
#         l -= 1
#         i -= 1
#
#     i += 1
#
# print(*lst_in)

# print(*range(1,20,3))

# lst = list(map(int,input().split()))
# s = 0
# for x in lst:
#     if abs(x) % 2 == 1:
#         s += x
#
# print(s)

# lst = input().split()
# for i in range(len(lst)):
#     lst[i] = len(lst[i])
#
# print(*lst)
#
# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
# print(i)

# n = int(input())
# flag = 1
# for i in range(2,n):
#     if n % i == 0:
#         flag = 0
#         break
# print('ДА' if flag else 'НЕТ')

# lst = input().lower().split()
# flag = 'ДА'
# for i in range(len(lst)-1):
#     if lst[i][-1] in ['ь', 'ъ', 'ы']:
#         if lst[i][-2] != lst[i+1][0]:
#             flag = 'НЕТ'
#             break
#     else:
#         if lst[i][-1] != lst[i+1][0]:
#             flag = 'НЕТ'
#             break
#
# print(flag)

# n = int(input())
# s = 0
# for i in range(1,n):
#     if i % 3 == 0 or i % 5 == 0:
#         s += i
#
# print(s)

# s = input()
# start = 0
# # print(s.find('ра'))
# # print(s.count('ра'))
# if s.count('ра') > 0:
#     for i in range(s.count('ра')):
#         print(s.find('ра',start), end = ' ')
#         start = s.find('ра',start)+1
#         # print(start)
#
# else:
#     print(-1)

# +7(xxx)xxx-xx-xx
# nomer = input()
# fl = 'ДА'
# if nomer[0] != '+':
#     fl = 'НЕТ'
# if nomer[1] != '7':
#     fl = 'НЕТ'
# if nomer[2] != '(':
#     fl = 'НЕТ'
# if nomer[6] != ')':
#     fl = 'НЕТ'
# if nomer[10] != '-':
#     fl = 'НЕТ'
# if nomer[13] != '-':
#     fl = 'НЕТ'
#
# for i in range(3,len(nomer)):
#     if i == 6 or i == 10 or i == 13:
#         continue
#
#     if not nomer[i].isdigit():
#         fl = 'НЕТ'
#
# print(fl)

# stroka = input()
# while stroka.count(' '):
#     stroka=stroka.replace(' ', '')
#
# s = 0
# begin = 0
# # end = 0
# znak = 1
# for i in range(len(stroka)):
#     if stroka[i].isdigit():
#         # end = i
#         continue
#     else:
#         if i != 0:
#             s += int(stroka[begin:i]) if znak else -int(stroka[begin:i])
#         begin = i+1
#         znak = 0 if stroka[i] == '-' else 1
#
# s += int(stroka[begin:len(stroka)]) if znak else -int(stroka[begin:len(stroka)])
# print(s)

# str = '2323'
# print(int(str[0:0]))
# print('dsf  adg   adsg'.replace(' ',''))

# nam = list(map(int,input().split()))
# for i,n in enumerate(nam):
#     nam[i] = n*n
#
# print(*nam)

# nam = list(map(int,input().split()))
# lst=[]
# for i in nam:
#     lst.append(i)
#     lst.append(i)
# print(*lst)

# nam = list(map(float,input().split()))
# min=nam[0]
# for i in nam[1:]:
#     if i < min:
#         min = i
#
# print(min)

# nam = list(map(float,input().split()))
# for i,n in enumerate(nam):
#     if n < 0:
#         nam[i] = -1
#
# print(*nam)

# lst = input().split()
# it = iter(lst)
# print(next(it))
# print(next(it))

# s = input()
# it = iter(s)
# b = next(it)
# while b != ' ':
#     print(b,end = '')
#     b = next(it)

# s = input()
# it = iter(s)
# for i in s:
#     print(next(it),end = ' ')

# N = int(input())
# m = []
# for i in range(N):
#     m.append([1]*N)
#
# for i in range(N):
#     m[i][N-1] = 5
#
# for i in m:
#     for j, x in enumerate(i):
#         print(x) if j == N-1 else print(x, end =' ')

# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['django chto eto takoe poryadok ustanovki', 'model mtv marshrutizaciya funkcii predstavleniya', 'marshrutizaciya obrabotka isklyucheniy zaprosov perenapravleniya']
# for i,st in enumerate(lst_in):
#     while st.count('  '):
#         lst_in[i]=lst_in[i].replace('  ', ' ')
#
#     lst_in[i]=lst_in[i].replace(' ', '-')
#
# for st in lst_in:
#     print(st)

# n = int(input())
# pr = []
# for i in range(2,n):
#     fl = 1
#     for j in range(2,i):
#         if i % j == 0:
#             fl = 0
#             break
#
#     if fl == 1:
#         pr.append(i)
#
# print(*pr)

# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# fl = 'ДА'
# for i,row in enumerate(lst_in):
#     for j,x in enumerate(row):
#         if x == 1:
#             s = 0
#             for ii in range(i-1 if i-1 >=0 else 0, i+2 if i+2 <= len(lst_in) else len(lst_in)):
#                 for jj in range(j-1 if j-1 >=0 else 0, j+2 if j+2 <= len(row) else len(row)):
#                     s += lst_in[ii][jj]
#
#             if s > 1:
#                 fl = 'НЕТ'
#                 break
#
#     if fl == 'НЕТ':
#         break
#
# print(fl)

# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# fl = 'ДА'
# for i in range(5):
#     for j in range(i+1,5):
#         if lst_in[i][j] != lst_in[j][i]:
#             fl = 'НЕТ'
#             break
#
#     if fl == 'НЕТ':
#         break
#
# print(fl)

# lst = list(map(int,input().split()))
# for i in range(len(lst)):
#     ii = i
#     for j in range(i+1,len(lst)):
#         if lst[j] <= lst[ii]:
#             ii = j
#
#     lst[i], lst[ii] = lst[ii], lst[i]
#
# print(*lst)

# lst = list(map(int,input().split()))
# for i in range(len(lst)-1):
#     for j in range(len(lst)-i-1):
#         if lst[j] > lst[j+1]:
#             lst[j+1], lst[j] = lst[j], lst[j+1]
#
# print(*lst)

# n = int(input())
# lst = [1, 2, 4, 8, 16, 32, 64]
# lst.sort(reverse=True)
# for x in lst:
#     for i in range(n // x):
#         print(x, end = ' ')
#     n -= x*(n // x)

# lst = input().split()
# lst_abs = [abs(float(x)) for x in lst]
# print(lst_abs)

# l = input()
# lst = [int(x) for x in l]
# print(lst)

# N = int(input())
# m = [[1 if i == x else 0 for x in range(N)] for i in range(N)]
# [print(*i) for i in m]

# lst = [city for city in input().split() if len(city) > 5]
# print(*lst)

# n = int(input())
# lst = [x for x in range(1,n+1) if n % x == 0]
# print(*lst)

# N = int(input())
# m = [[i for j in range(N)] for i in range(N)]
# [print(*x) for x in m]

# lst = list(map(float,input().split()))
# l = [lst[i] for i in range(len(lst)) if i % 2 == 0]
# print(*l)

# l1 = [int(x) for x in input().split()]
# l2 = [int(x) for x in input().split()]
# l = [x + l2[i] for i, x in enumerate(l1)]
# print(*l)

# cities_population = input().split()
# lst = [[city, int(cities_population[i+1])] for i, city in enumerate(cities_population) if i % 2 == 0]
# print(lst)

# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# lst = [x for row in lst_in for x in row][::-1]
# print(*lst)

# lst = list(map(int, input().split()))
# n = int(len(lst)**0.5)
# l = [[lst[i*n + j] for j in range(n)] for i in range(n)]
# print(l)

# t = ["– Скажи-ка, дядя, ведь не даром",
#     "Я Python выучил с каналом",
#     "Балакирев что раздавал?",
#     "Ведь были ж заданья боевые,",
#     "Да, говорят, еще какие!",
#     "Недаром помнит вся Россия",
#     "Как мы рубили их тогда!"
#     ]
#
# lst = [[x for x in row.split() if len(x) > 3] for row in t]
# print(lst)

# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# A = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
#
# for row in A:
#     print(*row)

# lst = [[x.split(sep = '=')[0],int(x.split(sep = '=')[1])] for x in input().split()]
#
# # for i in range(len(lst)):
# #     lst[i][1] = int(lst[i][1])
# # print(lst)
# d = dict(lst)
# # print(d)
# print(*sorted(d.items()))

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst = [[x.split(sep = '=')[0], x.split(sep = '=')[1]] for x in lst_in]
# d = {}
# for k,v in lst:
#     d[int(k)] = v
# print(*sorted(d.items()))

# lst = [[x.split(sep = '=')[0], x.split(sep = '=')[1]] for x in input().split()]
# d = dict([x.split(sep = '=') for x in input().split()])
# print(d)
# # d = {}
# # for k,v in lst:
# #     d[k] = v
#
# l = ['house', 'True', '5']
# fl = 'ДА'
# for x in l:
#     if x not in d:
#         fl = 'НЕТ'
#         break
#
# print(fl)
# print(d)

# d = dict([x.split(sep = '=') for x in input().split()])
# l = ['False', '3']
# for x in l:
#     if x in d:
#         del d[x]
#
# print(*sorted(d.items()))

# lst = input().split()
# d = {}
# for x in lst:
#     if x[:2] in d:
#         d[x[:2]].append(x)
#     else:
#         d[x[:2]] = [x]
# print(*sorted(d.items()))

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # print(lst_in)
# d = {}
# for x in lst_in:
#     if x.split()[1] not in d:
#         d[x.split()[1]] = [x.split()[0]]
#     else:
#         d[x.split()[1]].append(x.split()[0])
#
# print(*sorted(d.items()))

# a = 1
# lst = []
# while a:
#     a = int(input())
#     lst.append(a)
#
# lst.pop()
# d = {}
# for x in lst:
#     if x in d:
#         print(f'значение из кэша: {d[x]}')
#     else:
#         d[x] = round(x**0.5,2)
#         print(d[x])

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for x in lst_in:
#     if x in d:
#         print(f'Взято из кэша: {d[x]}')
#     else:
#         d[x] = 'HTML-страница для адреса ' + x
#         print(d[x])

# morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
# name = input().lower()
# out = ''
# for b in name:
#     out += (morze.get(b) + ' ')
# print(out.strip())

# morze_e = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
# lst_rev = []
# for key, value in morze_e.items():
#     lst_rev.append([value, key])
# morze_rev = dict(lst_rev)
#
# lst = input().split()
# row = ''
# for i in lst:
#     row += morze_rev[i]
#
# print(row)

# lst = list(map(int,input().split()))
# d = dict.fromkeys(lst)
# l = list(d.keys())
# print(*l)

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # print(lst_in)
# d = {}
# for x in lst_in:
#     if x.split()[0] not in d:
#         d[x.split()[0]] = [x.split()[1]]
#     else:
#         d[x.split()[0]].append(x.split()[1])
# for k,v in d.items():
#     print(f'{k}: ', end = '')
#     s = ''
#     for x in v:
#         s += x + ', '
#
#     print(s.strip(' ,'))

# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
# N = int(input())*1000
# s = 0
# while things:
#     km=''
#     vm=0
#     for k,v in things.items():
#         if v > vm:
#             km,vm = k,v
#
#     if s + vm > N:
#         things.pop(km)
#         continue
#     else:
#         s += vm
#         print(km, end=' ')
#         things.pop(km)

# d = {'banana': 3, 'apple': 2, 'cherry': 5}
# sorted_keys = sorted(d)
# print(sorted_keys)
#
# d = {'banana': 3, 'apple': 2, 'cherry': 5}
# sorted_by_value = sorted(d.items(), key=lambda item: item[1])
# print(sorted_by_value)

# x = 5
# y = x
# x += 1
# print(x)  # 6
# print(y)

# t = (3.4, -56.7)
# lst = map(int,input().split())
# t += tuple(lst)
# print(t)
# print(type(lst))

# lst = input().split()
# t = tuple(lst)
# if 'Москва' not in t:
#     t += ('Москва',)
# print(*t)

# lst = input().split()
# t = tuple(lst)
# while 'Ульяновск' in t:
#     lst = list(t)
#     del lst[lst.index('Ульяновск')]
#     t = tuple(lst)
# print(*t)

# t = tuple(input().split())
# for x in t:
#     if 'ва' in x.lower():
#         print(x.lower(), end = ' ')

# t = tuple(input().split())
# u = ()
# for x in t:
#     if x not in u:
#         u += (x,)
#
# print(*u)

# t = tuple(input().split())
# l = []
# for i,x in enumerate(t):
#     if t.count(x) > 1:
#         l.append(i)
#
# print(*l)

# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(input())
# t2 = ()
# for i in range(N):
#     t2 += (t[i][:N],)
#
# # print(t2)
# for row in t2:
#     print(*row)

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# t = ()
# for x in lst_in:
#     t += (tuple(x.split()),)
# print(t)

# s = set(map(float,input().split()))
# print(*sorted(s))

# s = input().lower().split()
# print(len(set(s)))

# str = input()
# s =  set()
# for c in str:
#     if c.isdigit():
#         s.add(c)
# if len(s) > 0:
#     print(*sorted(s))
# else:
#     print('НЕТ')

# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# s = set(lst_in)
# print(len(s))

# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# l = []
# for x in lst_in:
#     l.append(x.split(sep = ':')[0])
#
# print(len(set(l)))

# city = input()
# s = set()
# while city != 'q':
#     s.add(city)
#     city = input()
#
# print(len(s))

# l1 = list(map(int,input().split()))
# l2 = list(map(int,input().split()))
# s1 = set(l1)
# s2 = set(l2)
# print(*sorted(s1 ^ s2))

# l1 = input().split()
# l2 = input().split()
# s1 = set(l1)
# s2 = set(l2)
# print('ДА' if s1 == s2 else 'НЕТ')

# s = set(list(map(int,input().split())))
# print('НЕ ДОПУЩЕН' if 2 in s else 'ДОПУЩЕН')

# l1 = set(input().split())
# l2 = set(input().split())
# print('ДА' if l2 >= l1 else 'НЕТ')

# l = [2, 3, 5, 7]
# n = int(input())
# kontrol = {2,3,5}
# s = {1}
# for x in l:
#     while n % x == 0:
#         s.add(x)
#         n/=x
#
# print('ДА' if s >= kontrol else 'НЕТ')

# s = input().split()
# d = {int(s[0]) + i-1: s[i] for i in range(1,len(s))}
# # print(d)
# print(d[4])

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# mn = {x for x in lst_in}
# print(len(mn))

# lst = input().lower().split()
# words = {x for x in lst if len(x) >= 3}
# print(len(words))

# lst = input().lower().split()
# words = {x:lst.count(x) for x in lst}
# if 'и' in words:
#     print(words['и'])
# else:
#     print(0)

# import sys
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# # print(lst_in)
# d = {x:{i.split(':')[1].strip() for i in lst_in if i.split(':')[0] == x} for x in {ath.split(':')[0] for ath in lst_in}}
# # print(d)

# for (t := x) in range(10):
#     print(t)

# lst = [
#     row1 := [1, 2, 3],
#     row2 := [-1, 12, -13],
#     row3 := [7, 8, 2],
# ]
# print(lst)
# row1, row3 = row3, row1
# print(lst)
# row1[1]=100
# print(lst)
# # print(row1)
# lst[0], lst[-1] = row3, row1
# print(lst)

# t = tuple(map(int, input().split()))  # кортеж из целых чисел (в программе не менять)
# s = 0  # начальное значение суммы элементов
# lst = [(s:= s + x) for x in t]
# print(*lst)

# s = 0
# while (x:=int(input())) !=0:
#     if x % 2 == 0:
#         s+=x
#
# print(s)

# import math
# print(math.comb(10,8)*0.5**10)

# def f(x):
#     return abs(x) ** 0.5 + 3.2 + x
# t = tuple(map(float, input().split()))  # кортеж t в программе не менять
# lst = [[y:=f(x),y**2,y**3] for x in t]
# print(lst)

# p = 1
# while (x:=int(input())) > 0:
#     if x % 3 == 0:
#         p *= x
#
# print(p)

# def pr(weight):
#     print(f'Предмет имеет вес: {weight} кг.')
#
# pr(float(input()))

# def pr(lst):
#     print(f'Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}')
#
# lst = list(map(int,input().split()))
# pr(lst)

# def pr(width, height):
#     print(f'Периметр прямоугольника, равен {2*(width + height)}')
#
#
# width, height = list(map(int,input().split()))
# pr(width, height)

# def pr(mail):
#     fl = 1
#     if mail.count('.') == 1 and mail.count('@') == 1:
#         mail = mail.replace('.','')
#         mail = mail.replace('@', '')
#         # print(mail)
#         for x in mail:
#             if (not (ord('a') <= ord(x) <= ord('z'))) and (not (x in '0123456789_')):
#                 fl = 0
#                 break
#     else:
#         fl = 0
#
# print('ДА' if fl else 'НЕТ')
#
#
# mail = input().lower()
# pr(mail)

# def get_sq(x):
#     return x**2
#
# x = float(input())
# print(get_sq(x))

# def is_triangle(a,b,c):
#     return True if (a < b + c) and (b < a + c) and (c < a + b) else False
#
# def is_large(word):
#     return False if len(word) < 3 else True

# def even(x):
#     return x % 2 == 0
#
# while (x:=int(input())) != 1:
#     if even(x):
#         print(x)

# def not_even(x):
#     return not x % 2 == 0
#
#
# lst_d = list(map(int, input().split()))
# lst = [x for x in lst_d if not_even(x)]
# print(*lst)

# tp = input().strip()
# if tp == 'RECT':
#     def get_sq(a,b):
#         return a*b
# else:
#     def get_sq(a):
#         return a*a

# def long(word):
#     return len(word) >= 6
#
#
# cities = input().split()
# lst = [x for x in cities if long(x)]
# print(*lst)

# def long(word):
#     return word, len(word)
#
#
# cities = input().split()
# d = {long(x)[0]:long(x)[1] for x in cities}
# a = sorted(d, key=d.get)
# print(*a)

# digs = list(map(int,input().split()))
# def prod(a,b):
#     return a*b
#
# print(prod(max(digs),min(digs)))

# def get_nod(a, b):
#     if a < b:
#         b, a = a, b
#
#     while b != 0:
#         a, b = b, a % b
#
#     return a
#
#
# print(get_nod(15, 121050))

# def get_rect_value(a,b,tp = 0):
#     if tp == 0:
#         return 2*(a+b)
#     else:
#         return a*b
#
# print(get_rect_value(2,2,1))

# def check_password(pwd, chars = '$%!?@#'):
#     if len(pwd) < 8:
#         return False
#     else:
#         fl = 0
#         for s in chars:
#             if s in pwd:
#                 fl = 1
#                 break
#
#         return True if fl else False
#
#
# print(check_password('123fdsggh4@'))
# print(set('123fdsg!gh4') & set('$%!?@#'))

# def to_latin(s, sep = '-'):
#     out = ''
#     s = s.lower().strip()
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#     for x in s:
#         if x in t:
#             out += t[x]
#         else:
#             out += x
#     return out.replace(' ', sep)
#
#
#
# s = input()
# print(to_latin(s))
# print(to_latin(s,'+'))


# def make_tag(s,tag = 'h1', up = True):
#     if up:
#         return f'<{tag.upper()}>{s}</{tag.upper()}>'
#     else:
#         return f'<{tag}>{s}</{tag}>'
#
#
# s = input()
# print(make_tag(s,'div'))
# print(make_tag(s,'div', False))

# def get_even(*args):
#     lst = [x for x in args if x % 2 == 0]
#     return lst
#
# print(get_even(45,4,8,11,12,0))

# def get_biggest_city(*args):
#     m = 0
#     city = ''
#     # print(type(args))
#     # print(args)
#     for x in args:
#         # print(x)
#         if len(x) > m:
#             city = x
#             m = len(x)
#             # print(city)
#
#     return city
#
# s = input().split()
# # print(s)
# print(get_biggest_city(*s))

# def get_data_fig(*args, **kwargs):
#     perim = sum(args)
#     t = (perim,)
#     # for k in kwargs:
#     #     t = t + (kwargs[k],)
#     if 'tp' in kwargs:
#         t = t + (kwargs['tp'],)
#     if 'color' in kwargs:
#         t = t + (kwargs['color'],)
#     if 'closed' in kwargs:
#         t = t + (kwargs['closed'],)
#     if 'width' in kwargs:
#         t = t + (kwargs['width'],)
#     return(t)
#
#
# print(get_data_fig(1,2,3,4,5, color=32,tp=False))

# import sys
#
# def is_isolate(i,j,lst_2d):
#     if lst_2d[i][j]+lst_2d[i][j+1]+lst_2d[i+1][j]+lst_2d[i+1][j+1] > 1:
#         return False
#     else:
#         return True
#
#
#
# def verify(lst_2d):
#     n = len(lst_2d)
#     # print(n)
#     for i in range(n-1):
#         for j in range(n-1):
#             if lst_2d[i][j] == 1:
#                 if not is_isolate(i,j,lst_2d):
#                     return False
#
#     for i in range(1,n-1):
#         if lst_2d[n-1][i] == 1:
#             if lst_2d[n-1][i-1]+lst_2d[n-1][i]+lst_2d[n-1][i+1] > 1:
#                 return False
#
#         if lst_2d[i][n-1] == 1:
#             if lst_2d[i-1][n-1]+lst_2d[i][n-1]+lst_2d[i+1][n-1] > 1:
#                 return False
#
#     return True
#
#
# lines = sys.stdin.readlines()  # чтение строк из входного потока (переменную lines не менять)
# lst2D = [list(map(int, x.strip().split())) for x in lines]  # формирование матрицы чисел
#
# print(verify(lst2D))

# def  str_min(s1,s2):
#     return s1 if s1 < s2 else s2
#
# def str_min3(s1,s2,s3):
#     return str_min(s1,str_min(s2,s3))
#
# def str_min4(s1,s2,s3,s4):
# #     return str_min(str_min(s1,s2),str_min(s3,s4))
#
# # *lst, x, y, z = map(int, input().split())
# # print(*lst)
#
# print(map(int, input().split()))
#
# lst = input().split()
# lst_c = (*lst,)
# print(lst_c)

# a, b = map(int, input().split())
# lst = [*range(a,b+1)]
# print(*lst)

# nums = input().split()
# cities = input().split()
# lst = [*nums, *cities]
# print(*lst)
#
# import sys
#
# # считывание списка из входного потока
# lst_in = [[x.split(sep = '=')[0],x.split(sep = '=')[1]] for x in list(map(str.strip, sys.stdin.readlines()))]
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# menu = {**menu,**dict(lst_in)}
# print(menu)
#
# def get_rec_N(N):
#     if N > 0:
#         get_rec_N(N-1)
#         print(N)
#
# # get_rec_N(8)
#
# def get_rec_sum(lst):
#     s = 0
#     if lst:
#         s += lst.pop()
#         s += get_rec_sum(lst)
#     return s
#
# lst = list(map(int,input().split()))
# print(get_rec_sum(lst))
#
# def fib_rec(N, f=[1, 1]):
#     if len(f) < N:
#         f.append(f[-1] + f[-2])
#         fib_rec(N, f)
#
#     return f
#
#
# N = int(input())
# print(fib_rec(N))

# def fact_rec(n):
#     if n < 2:
#         return 1
#     return n*fact_rec(n-1)
#
#
# n = int(input())
#
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# def get_line_list(d,a=[]):
#     for x in d:
#         if type(x) == list:
#             get_line_list(x,a)
#         else:
#             a += [x]
#     return a
#
# print(get_line_list(d))

# def get_path(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return get_path(n-1) + get_path(n-2)
#
# N = int(input())
# print(get_path(N))


# def split(lst):
#     l = len(lst)
#     if l == 1:
#         return lst, []
#     elif l == 2:
#         return lst[0],lst[1]
#     else:
#         split(lst[: (l // 2)])
#         split(lst[(l // 2) :])
#
#
# def join_sorted(lst1,lst2):
#     i1,i2 = 0,0
#     res = []
#     while i1 < len(lst1) and i2 < len(lst2):
#         if lst1[i1] <= lst2[i2]:
#             res.append(lst1[i1])
#             i1 += 1
#         else:
#             res.append(lst2[i2])
#             i2 += 1
#
#     if i1 == len(lst1):
#         res = res + lst2[i2:]
#     else:
#         res = res + lst1[i1:]
#
#     return res
#
#
# def sort(lst):
#     while len(lst)>1:
#         a, b = lst.pop(0), lst.pop(0)
#         if type(a) != list:
#             a = [a]
#         if type(b) != list:
#             b = [b]
#         lst.append(join_sorted(a,b))
#
#     return lst[0]
#
#
# lst = list(map(int, input().split()))
# print(*sort(lst))
# print(split(lst))
# print(join_sorted([],[2,7,8]))
#
# get_sq = lambda x: x**2
# print(get_sq(2))

# get_div = lambda a,b: None if b == 0 else a/b

# x = float(input())
# m = lambda x: x if x >= 0 else -x
# print(m(x))


# print((lambda x: x if x >= 0 else -x)(float(input())))
# print((lambda x: True if 'ra' in x else False)(input()))

# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
#
# digs = list(map(int,input().split()))
# print(*filter_lst(digs))
# print(*filter_lst(digs,lambda x: x < 0))
# print(*filter_lst(digs,lambda x: x >= 0))
# print(*filter_lst(digs,lambda x: 3 <= x <= 5))

# WIDTH = int(input())
#
#
# def func1():
#     global WIDTH
#     WIDTH += 1
#     return WIDTH
#
#
# print(func1())

# def func1():
#     msg = input()
#
#
#     def func2():
#         nonlocal msg
#         msg = input()
#         print(msg)
#
#
#     func2()
#     print(msg)
#
#
# func1()

# def create_global(x):
#     global TOTAL
#     TOTAL = x
#
#
# create_global(10)
# print(TOTAL)

# str= 'dsfsg'
# def outter():
#     # global str
#     str = 'qwreqw'
#     print(str)
#     def inner():
#         # global str
#         # str = str + 'zxcv'
#         print(str)
#
#     inner()
#     print(str)
#
# outter()
# print(str)

# def counter(start = 0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#
#     return step
#
# c1 = counter(10)
# c2 = counter(10)
#
# print(c1())
# print(c1())
# print(c1())
# print(c2())

# def counter_add(n):
#     def func(par):
#         return par+n
#
#     return func
#
#
# cnt = counter_add(2)
# k = int(input())
# print(cnt(k))

# def fun_out(tag):
#     def fun_in(str):
#         return f'<{tag}>{str}</{tag}>'
#
#     return fun_in
#
#
#
# tag = input()
# str = input()
# f = fun_out(tag)
# print(f(str))

# def fun_out(tp):
#     def fun_in(str):
#         if  tp == 'list':
#             return list(map(int,str.split()))
#         else:
#             return tuple(map(int, str.split()))
#
#     return fun_in
#
#
#
# tp = input()
# str = input()
# f = fun_out(tp)
# print(f(str))

# def func_show(f):
#     def inner(*args,**kwargs):
#         print(f'Площадь прямоугольника: {f(*args,**kwargs)}')
#
#     return inner
#
# @func_show
# def get_sq(width, height):
#     return width*height
#
# get_sq(4,5)

# def show_menu(f):
#     def wrapper(*args):
#         for i,name in enumerate(f(*args)):
#             print(f'{i+1}. {name}')
#
#     return wrapper
#
# menu = input()
#
# @show_menu
# def get_menu(s):
#     return s.split()
#
# get_menu(menu)

# def sort(f):
#     def wrapper(*args):
#         return sorted(f(*args))
#
#     return wrapper
#
# s = input()
#
# @sort
# def get_list(s):
#     return  list(map(int,s.split()))
#
# print(*get_list(s))

# def make_dict(f):
#     def make_d(*args,**kwargs):
#         eng_lst,ru_lst = f(*args,**kwargs)
#         return {eng_lst[i]:ru_lst[i] for i in range(len(ru_lst))}
#     return make_d
#
# eng_words = input()
# ru_words = input()
#
# @make_dict
# def make_tuple(eng,ru):
#     return tuple(eng.split()), tuple(ru.split())
#
# print(*sorted(make_tuple(eng_words,ru_words).items()))

# def remove_repeat(f):
#     def wrap(*args,**kwargs):
#         s = f(*args,**kwargs)
#         while '--' in s:
#             s = s.replace('--','-')
#         return s
#     return wrap
#
# @remove_repeat
# def translit(s):
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#     s = s.lower()
#     out_s = ''
#     for x in s:
#         if x in t:
#             out_s += t[x]
#         elif x in ' : ;.,_':
#             out_s += '-'
#         else:
#             out_s += x
#
#     return out_s
#
#
# s = input()
# print(translit(s))

# def decor(start = 0):
#     def decor_in(func):
#         def wrapper(*args,**kwargs):
#             return start + func(*args,**kwargs)
#         return wrapper
#     return decor_in
#
# @decor(5)
# def sum_int(n):
#     return sum(list(map(int,n.split())))
#
# n = input()
# print(sum_int(n))

# from functools import wraps
#
#
# def decor(tag='h1'):
#     def decor_in(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#
#         return wrapper
#
#     return decor_in
#
#
# @decor('div')
# def low(s):
#     return s.lower()
#
#
# s = input()
# print(low(s))
#
# from functools import wraps

# def decor_param(chars = ' !?'):
#     def decor_in(func):
#         # @wraps
#         def wrapper(*args,**kwargs):
#             out_s = ''
#             s = func(*args,**kwargs)
#             for x in s:
#                 if x in chars:
#                     out_s += '-'
#                 else:
#                     out_s += x
#             while '--' in out_s:
#                out_s = out_s.replace('--','-')
#             return out_s
#         return wrapper
#     return decor_in
#
# @decor_param("?!:;,. ")
# def translit(s):
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#          'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#          'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#          'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#     s = s.lower()
#     out_s = ''
#     for x in s:
#         out_s += t.get(x,x)
#
#     return out_s
#
#
# s = input()
# print(translit(s))
#
# from functools import wraps
#
# def decor(f):
#     @wraps(f)
#     def wrap(*args):
#         return sum(f(*args))
#     return(wrap)
#
#
# @decor
# def get_list(x):
#     '''Функция для формирования списка целых значений'''
#     return list(map(int,x.split()))
#
# s = input()
# print(get_list(s))
# print(get_list.__doc__)
# print(get_list.__name__)

# import math
# n = float(input())
# print(math.ceil(n))

# from math import floor
# n = float(input())
# print(floor(n))

# from math import factorial as fact

# from random import seed, randint
# seed(1)
# print(randint(10, 50))

# from random import seed, random as rnd
# seed(10)
# print(round(rnd(), 2))

from math import floor as fl, ceil as cl, pi


def ff(d):
    print(d)
