def make_accumulator(start=0):
    total=start
    def add(val):
        nonlocal total
        total+=val
        return total
    return add
a=make_accumulator(5)
print(a(2))
print(a(8))
print(a(9))