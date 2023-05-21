# создать функцию можно через def, а можно 
# с использованием синтаксиса lambda
def mult(x, y):
    return x * y

# а можно было так:
mult = lambda x, y: x * y

def calc(op, a, b):# здесь в качестве первого параметра передаётся функция
    return op(a, b)

print(calc(mult, 4, 6)) 

#====================================
# ввод данных с клавиатуры через пробел (например, 1 6 9 12)
# list comprehension
my_list = [int(x) for x in input().split()]
# а можно через map
my_list = list(map(int, input().split()))


# функция filter
data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data)))
print(res) # [0, 2, 4, 6, 8]


# функция zip
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)

# функция enumerate
users = ['user1', 'user2', 'user3', 'user4', 'user5']
for index, name in enumerate(users):
    print(index, name)

# как в Python можно работать с кортежами
a = (1, 4)
x, y = a
