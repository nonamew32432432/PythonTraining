true_list = []
false_list = []

words = input('Введите список живоных: \n')
length = int(input('Введите длинну слов: \n'))

def partition(words, length, true_list, false_list):
    words = [i.strip() for i in words.split(',')]
    for i in words:
        if len(i) == length:
            true_list.append(i)
        else:
            false_list.append(i)
    return true_list, false_list

print(partition(words, length, true_list, false_list))