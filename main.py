# This is a sample Python script.

# homeworck 4.1

# numbersList = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# newNumbersList = []
# listSpaceCounter = 0
# lengthOfList = len(numbersList)
# i = 0
#
# while i < lengthOfList: # цикл длится пока не закончится список
#     if numbersList[i] == 0: # если ячейка = 0 добавляю 0 в конец нового списка
#         newNumbersList.append(0)
#     else:
#         newNumbersList.insert(listSpaceCounter, numbersList[i]) # в ином случае добавляю в новый список по адресу listSpaceCounter
#         listSpaceCounter += 1
#     i += 1
# print(newNumbersList)

# homeWorck 4.2

# numbersList = [0, 1, 7, 2, 4, 8]
# multiplicationNumbers = 0
# lengthOfList = len(numbersList)
# a = 0
# i = 0
# if len(numbersList) != 0: # проверка наличия элементов в списке.
#     while i < lengthOfList:
#         if i % 2 == 0: # отбираю элементы с парными индексами
#          multiplicationNumbers += numbersList[i] # суммирую все эти элементы
#         i += 1
#     print(multiplicationNumbers * numbersList[-1]) # сумму всех отобраных чисел умножаю на последний элемент списка
# else:
#     print(0)

# homeWork 4.3

import random
list = []
listOfTree = []
listLang = random.randrange(3,11) # создаю случайную длину списка
i = 0

while i < listLang:
    list.append(random.randrange(0,10)) # наполняю список случайными числами
    i +=1

listOfTree.append(list[0])
listOfTree.append(list[2])
listOfTree.append(list[-2])
print(list)
print(listOfTree)