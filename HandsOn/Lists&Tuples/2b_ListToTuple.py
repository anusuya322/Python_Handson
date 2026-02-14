n=int(input("Enter the size:"))
li=[]
for i in range(n):
    num=input()
    li.append(num)
print(li)
res=[]
i=0
while i<len(li)-1:
    tup=tuple(li[i:i+2])
    res.append(tup)
    i=i+2
print(res)