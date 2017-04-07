
listOfWords = ['Anoush', 'Ashkhen', 'Arman', 'Nara']
def filter_long_words(list, n):
    newList = []
    for i in list:
        if len(i)>n:
            newList.append(i)
    return newList
print filter_long_words(listOfWords,5)


