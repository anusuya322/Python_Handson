def counter():
    count =0
    def next():
        nonlocal count
        count+=1
        return count
    return next
a=counter()
print(a())
print(a())
print(a())
print(a())
print(a())