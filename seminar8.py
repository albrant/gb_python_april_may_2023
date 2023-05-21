# запись данных в файл построчно
data = [45, 46, 79]
data = list(map(lambda x: str(x) + '\n', data))
with open('1.txt', 'w') as f:
    f.writelines(data)

# чтение данных из файла, занесение в список
my_list = []
with open('1.txt', 'r') as f:
    for i in f:
        my_list.append(int(i))
print(my_list)

# а можно было и так:
my_list = [int(x) for x in open('1.txt', 'r')]

# import os

# os.chdir('C:/Users/79190/PycharmProjects/GB')
# directory = os.getcwd()

# os.path.basename()
# print(os.path.abspath('seminar8.py')) 

# import shutil
# shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst.
# shutil.copy(src, dst) - копирует содержимое файла src в файл **или папку** dst.
# shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path должен указывать на директорию, а не на символическую ссылку.