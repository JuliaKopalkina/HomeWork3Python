# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний 
# и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]

def MyltiplyList (lst):
    for i in range(len(lst)):
      lst[i]= (lst[i]*lst[-1-i])
    return(lst) 

def NewList (lst):
    if len(lst)%2 == 0:
        return(lst[0:len(lst)//2])
    else:
        return(lst[0:len(lst)//2+1])

    
MyltiplyList(list1)
print(NewList(list1))
MyltiplyList(list2)
print(NewList(list2))