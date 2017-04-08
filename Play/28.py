def find_longest_word(list):
    newList = map(len, list)
    return reduce(max, newList)

print find_longest_word(['Anoush', 'Ashkhen', 'Tamara'])