
def reverse(inputString):
    reversString =""
    for i in range(0, len(inputString)):
        reversString = reversString + inputString[-i-1]
    return reversString

print reverse("I am testing")


