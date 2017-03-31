def translate(robber):
    newWord = ''
    consonants = 'bcdfghjklmnpqrstvwxz'
    for letter in robber:
        if letter in consonants:
            newWord += letter + 'o' + letter
        else:
            newWord +=letter
    return newWord
print(translate("this is fun"))

