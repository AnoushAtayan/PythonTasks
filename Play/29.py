def filter_long_words(list, n):
    return filter(lambda x:len(x)>n, list)

print filter_long_words(['Anoush', 'Ashkhen', 'Tamara'], 6)