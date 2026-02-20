def make_multiplier(k):
    def multiplier(num):
         return num*k
    return multiplier
num=int(input("Enter a number:"))
k=int(input("Enter k value:"))
a=make_multiplier(k)
print(a(num))