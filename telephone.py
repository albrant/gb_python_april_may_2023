def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data


def printinfo(data):
    for i in data:
        print(i)


def export():
    pass

def main():
    my_choice = -1
    data = readfile('tel.txt')
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - вывести инфо на экран')
        print('2 - произвести экпорт данных')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {1: printinfo, 2: export}
        operations[my_choice](data)
        
            
    print('До свидания')


if __name__ == '__main__':
    main()
