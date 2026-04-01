li=[1,2,4,4,2,1,3,4,5,6]
freq={}
for n in li:
    freq[n]=freq.get(n,0)+1
print(freq)
sorted_li=sorted(freq.items(),key=lambda x:(-x[1],x[0]))#, reverse=True)
print(sorted_li)
res=[]
for num,count in sorted_li:
    for _ in range(count):
        res.append(num)
print(res)

