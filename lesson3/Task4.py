# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

DecNumber = int(input('Введите число: '))

def FromDecimalToBinary (number):
    result = ''
    while number > 0:
        result = str (number%2) +result
        number = number //2
    return result

if DecNumber == 0:
    print(f'Двоичное число: {0}')
else:
    print (f'Двоичное число: {FromDecimalToBinary(DecNumber)}')

