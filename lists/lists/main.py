myUniqueList = []
myLeftovers = []

def addElementToList(elementToAdd):
        if elementToAdd not in myUniqueList:
            myUniqueList.append(elementToAdd)
            return True
        else:
            redirectToLeftovers(elementToAdd)
            return False

def redirectToLeftovers(duplicate):
    myLeftovers.append(duplicate)

addElementToList(5)
addElementToList(6)
addElementToList(5)
addElementToList("hello")
addElementToList(10.5)
addElementToList("hello")
addElementToList(10.5)
addElementToList("sunny_day")
addElementToList(10.5)

print(myUniqueList)
print(myLeftovers)

print("First element in my uniqe list is " +  str(myUniqueList[0]))
