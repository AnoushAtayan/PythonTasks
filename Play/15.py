listOfWords = ['Anoush', 'Ashkhen', 'Arman', 'Nara']
def find_longest_word(list):
    max = 0
    for i in list:
        if len(i)> max:
            max = len(i)
    return max

print find_longest_word(listOfWords)
