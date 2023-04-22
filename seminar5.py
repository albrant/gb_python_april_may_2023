## стандартная реализация Фибоначчи через рекурсию (неоптимально)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(10):
    print(i, fib(i))


# Реализация Фибоначчи через рекурсию с дополнительным заполминанием 
# вычисленных элементов
def fib(n):
    if n < 2:
        temp[n] = n
        return n
    else:
        if temp[n] > 0:
            return temp[n]
        else:
            q = fib(n-1) + fib(n-2)
            temp[n] = q
            return q

temp = [0] * 100 # массив для запоминания 100 элементов ряда Фибоначчи
for i in range(100):
    print(i, fib(i))

#Реализация нахождения числа Фибоначчи без рекурсии (один из способов)

a = [0, 1]
n = 100
for i in range(2, n+1):
    a.append(a[i-1] + a[i-2])
print(a[-1])


# функция нахождения простого числа
def is_simple(n):
    for i in range(2, n**0.5+1):
        if n % i == 0:
            return False # сразу возвращаем False, то есть число не простое
    return True # если цикл пройдёт все числа и ни на что не разделится, то после цикла 
    # возвращаем True, зная, что число простое

n = int(input())
if is_simple(n):
    print('Число простое')
else:
    print('Число составное')
