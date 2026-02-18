n=int(input("Enter number of products:"))
pr=[]
for _ in range(n):
    pr.append(int(input()))
discount=map(lambda x:x-(x*0.1),pr)
filtered=filter(lambda x:x>=200,discount)
from functools import reduce
total=reduce(lambda x,y:x+y,filtered,0)
print("The total bill is: ",total)
