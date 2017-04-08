import re

def correct(inputString):
    #two or more occurrences of the space character is compressed into one
    correctedString = re.sub('\ +', ' ', inputString)
    # inserts an extra space after a period if the period is directly followed by a letter
    correctedString =  re.sub('\.', '. ', correctedString)
    return correctedString

print correct('This   is  very funny  and    cool.Indeed!')