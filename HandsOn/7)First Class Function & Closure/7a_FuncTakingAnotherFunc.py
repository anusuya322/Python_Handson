def apply_twice(func, x):
    return func(func(x))
def add(num):
    return num+num
x=int(input("Enter a number:"))
print(apply_twice(add,x))