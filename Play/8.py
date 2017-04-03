def is_palindrome(word):
    reverseWord = ""
    for i in range(0, len(word)):
        reverseWord = word[::-1]
        if word.lower()== reverseWord.lower():
            return True
        else:
            return False

print is_palindrome("MadaM")