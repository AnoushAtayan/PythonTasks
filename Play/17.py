
def isPalindrome(expression):
    newList = []
    for item in expression:
        if item.isalpha():
            newList.append(item.capitalize())
    print newList
    for i in range(len(newList)):
        if newList[i] == newList[len(newList)-1-i]:
            return True
        else:
            return False

print isPalindrome('Dammit, I\'m mad!')