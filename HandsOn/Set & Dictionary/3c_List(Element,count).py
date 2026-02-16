n=int(input("Enter size of list:"))
li=[]
for _ in range(n):
    li.append(int(input()))
d={}
for x in li:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print(d)
ans=list(d.items())
print(ans)
