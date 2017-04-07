import string

alphabet = list(string.ascii_lowercase)

def isPangram(sentence):
    newList = []
    for item in sentence:
        if item.isalpha():
            if item not in newList:
                newList.append(item.lower())
    sList = sorted(newList)
    if sList == alphabet:
        return True
    else:
        return False

print isPangram('The quick brown fox jumps over the lazy dog')

