def translate(englishList):
    dict =  {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
    swedishList = ''
    for i in englishList.split(' '):
        swedishList = swedishList +str(dict.get(i) + ' ')
    return  swedishList

print translate('merry christmas and happy new year')


