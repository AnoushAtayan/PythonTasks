def mean(x, *l):
    sum = x
    for i in l:
        sum+=i
    return sum/(1.0+len(l))

print mean(5, 6, 7)




