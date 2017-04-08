def make_3sg_form(verb):
    newVerb = ''
    if verb.endswith('y'):
        newVerb = verb[:-1] + 'ies'
    elif verb.endswith(('o',  'ch', 's', 'sh', 'x','z')):
        newVerb = verb + 'es'
    else:
        newVerb = verb + 's'
    return newVerb


print make_3sg_form('try')
