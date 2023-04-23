# задача с семинара о парах одинаковых чисел в списке
a = [int(i) for i in input().split()]
count = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count += 1
print(count)


# копирование списков
a = [1, 43, 86]
b = a # так нельзя!
# лучше так
b = a.copy()
# или так
b = [i for i in a]
