# This is a sample Python script.

# homeworck 4.1

numbersList = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
newNumbersList = []
listSpaceCounter = 0
lengthOfList = len(numbersList)
i = 0

while i < lengthOfList: # цикл длится пока не закончится список
    if numbersList[i] == 0: # если ячейка = 0 добавляю 0 в конец нового списка
        newNumbersList.append(0)
    else:
        newNumbersList.insert(listSpaceCounter, numbersList[i]) # в ином случае добавляю в новый список по адресу listSpaceCounter
        listSpaceCounter += 1
    i += 1
print(newNumbersList)
