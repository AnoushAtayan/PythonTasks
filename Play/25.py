
def make_ing_form(verb):
    newVerb = ''
    #If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
    if verb.endswith('e'):
        newVerb =   verb[:-1] + 'ing'
    #If the verb ends in ie, change ie to y and add ing
    elif verb.endswith('ie'):
        newVerb = verb[:-2] + 'ying'
    #For words consisting of consonant-vowel-consonant, double the final letter before adding ing
    elif verb[-1] not in "aeiou" and verb[-3] not in "aeiou" and  verb[-2] in "aeiou":
        newVerb =  verb + verb[-1] + 'ing'
    else:
        newVerb = verb+ 'ing'
    return newVerb

print make_ing_form('try')
print make_ing_form('hug')
print make_ing_form('move')