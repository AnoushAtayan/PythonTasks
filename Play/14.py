listOfWords = ['Anoush', 'Ashkhen', 'Arman', 'Nara']
def lengthOfWord(list):
    listOfIntegers = []
    for i in list:
        listOfIntegers.append(len(i))
    return listOfIntegers
print lengthOfWord(listOfWords)