string = "abbabcbdbabdbdbabababcbcbab"
def char_freq(word):
    dict = {}
    for letter in word:
        dict[letter] = 0
    for letter in word:
        dict[letter]+=1
    return dict

#simple version
import collections

def char_freq_simple(word):
    print collections.Counter(word)


print char_freq(string)
char_freq_simple("abbabcbdbabdbdbabababcbcbab")
