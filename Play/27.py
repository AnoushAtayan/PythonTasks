# using a for-loop
def mapsOfStringList_for(stringList):
    integerlist = []
    for i in stringList:
        integerlist.append(len(i))
    return integerlist

#using the higher order function map()

def mapsOfStringList_map(stringList):
    return map(len, stringList)

#using list comprehensions

def mapsOfStringList_lists(stringList):
    return [len(word) for word in stringList]


print mapsOfStringList_for(['Anoush', 'Ashkhen', 'Tamara'])
print mapsOfStringList_map(['Anoush', 'Ashkhen', 'Tamara'])
print mapsOfStringList_lists(['Anoush', 'Ashkhen', 'Tamara'])
