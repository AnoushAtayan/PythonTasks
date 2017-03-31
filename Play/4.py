
def vowel_check(input):
    list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for i in list:
        if input ==i:
            return True
        else:
            return False
print vowel_check('F')