list = [1, 2, 3, 4]

def sum(list):
    sum = 0
    for i in list:
        sum = sum+i
    return sum


def multiplies(list):
    multiple =1
    for i in list:
        multiple = multiple*i
    return multiple

print sum(list)
print multiplies(list)


