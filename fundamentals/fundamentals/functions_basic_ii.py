# Countdown

def countdown(x):
    newList = []
    for i in range(x, -1, -1):
        newList.append(i)
    return newList
newList = countdown(5)
print(newList) 


# Print and Return

def printAndReturn(myList):
    print(myList[0])
    return(myList[1])

printAndReturn([4,2])


# First Plus Length

def firstPlusLength(list):
    return list[0] + len(list)

print(firstPlusLength([1,2,3,4,5]))


# Values Greater than Second

def valuesGreater(list):
    newList = []
    count = 0
    if len(list) < 2:
        return False
    for i in list:
        if i > list[1]:
            count = count + 1
            newList.append(i)
    print(count)
    return newList


print(valuesGreater([5,2,3,2,1,4]))
print(valuesGreater([5]))


# This Length, That Value

def thisLength(size,value):
    newList = []
    for val in range(size):
        newList.append(value)
    return newList

print(thisLength(4,7))