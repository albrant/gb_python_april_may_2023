# a = []
# for i in range(10):
#     if i%2 == 0:
#         a.append(i)
# print(a)
# from random import randint

# a = [i for i in range(10) if i%2 == 0]
# print(a)

# a = [int(i) for i in input().split()]
# print(a)

# a = [0 for i in range(10)]

# создание словаря и добавление в него элементов
# my_dict = {}
# my_dict['first'] = 'Первый'
# my_dict['second'] = 2
# print(my_dict)

# пробежаться по словарю можно двумя способами
# способ 1
# for key in my_dict:
#     print(my_dict[key])
# способ 2
# for key, value in my_dict.items():
#     print(key, ' -> ', value)

# if 'first' in my_dict:
#     print('yes')
# print(my_dict['first'])

# a = [1, 3, 6, 8]
# a = tuple(a) # создание кортежа
# print(a[2])

# создание множества
# a = set([1, 4, 7, 3, 4])


# Профилирование и отладка:
# как оценить время выполнения задачи

# from time import time

# start = time()
# a = 0
# for i in range(10**7):
#     a += 1
# print(a)
# end = time()
# print(end - start)

# Как узнать, сколько памяти занимает переменная
# import sys
# a = 40
# print(sys.getsizeof(a))

# Решение двух задач с семинара
# задача 1
# st = 'a a a b c a a d c'
# my_dict = {}
# for i in st.split():
#     if i in my_dict:
#         print(f'{i}_{my_dict[i]}', end=' ')
#         my_dict[i] += 1
#     else:
#         print(i, end=' ')
#         my_dict[i] = 1

# задача 2
# text = 'I go to school every day to go I'
# print(len(set(text.split())))
