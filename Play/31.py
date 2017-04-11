# higher order function map()
def map(function, sequence):
    result =[]
    for i in sequence:
        result.append(function(i))
    return  result

# higher order function filter()

def filter(function, sequence):
    return{i for i in sequence if function(i) ==True}

# higher order function reduce()
def reduce(function,iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value
