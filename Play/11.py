def generate_n_chars(n, c):
    string =""
    for i in range(n):
        string=string + c
    return string
print generate_n_chars(5,"x")