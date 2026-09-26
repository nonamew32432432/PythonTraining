number = int(input('Введите число: \n'))

def evil_or_odious(number):
    binary_namber = bin(number)[2:]
    units = binary_namber.count('1')
    if units%2 == 0:
        return 'Its Evil!'
    else:
        return 'Its Odious!'

print(evil_or_odious(number))