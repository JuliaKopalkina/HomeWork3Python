# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
 
n = int(input('Введите число: '))

def StraightFib (n):
    NewList = []
    fib1 = fib2 = 1
    NewList.append(fib1)
    NewList.append(fib2)
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        NewList.append(fib2)
    return NewList


def ReverseFib (lst):
    NewList = []
    for i in range(len(lst)):
        if i%2==0:
            NewList.append(lst[i]*(-1))
        else:
            NewList.append(lst[i])
    return NewList


print(ReverseFib(StraightFib(n))[::-1]+StraightFib(n))
