list = [23, 30, 60, 80, 70, 55,35, 105,2000]
def max_of_three(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max

print max_of_three(list)