def mult(x, y):
    return x * y

# а можно было так:
mult = lambda x, y: x * y

def calc(op, a, b):
    return op(a, b)

print(calc(mult, 4, 6))

#====================================
# функция map
my_list = [int(x) for x in input().split()]
# а можно через map
my_list = list(map(int, input().split()))

# функция filter

# функция zip


#====================================
# enumerate
users = ['user1', 'user2', 'user3', 'user4', 'user5']
for index, name in enumerate(users):
    print(index, name)

a = (1, 4)
x, y = a
