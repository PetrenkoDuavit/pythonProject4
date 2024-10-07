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

numbersList = [0, 1, 7, 2, 4, 8]
multiplicationNumbers = 0
lengthOfList = len(numbersList)
a = 0
i = 0

while i < lengthOfList:
    if i % 2 == 0: # отбираю элементы с парными индексами
        multiplicationNumbers += numbersList[i] # суммирую все эти элементы
    i += 1
print(multiplicationNumbers * numbersList[-1]) # сумму всех отобраных чисел умножаю на последний элемент списка


