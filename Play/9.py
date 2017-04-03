list = ["Anoush", "Ash", 5, 6]

def is_member(x, a):
    return x.count(a)>0
print is_member(list, 5)