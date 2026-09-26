lists = input('Введите список чисел: \n')
lists = lists.split(' ')
lists = list(lists)
n = int(input('Введите сколько чисел вы хотите вывести: \n'))

print(lists[:n])