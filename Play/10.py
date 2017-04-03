def overlapping(list1, list2):
    return any(i == j for i in list1 for j in list2)
print overlapping([1, 5], [5, 4])