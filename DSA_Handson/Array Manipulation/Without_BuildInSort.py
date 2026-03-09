n=int(input("Enter the array size:"))
li=[]
for _ in range(n):
    li.append(int(input()))
freq={}
for i in li:
    freq[i]=freq.get(i,0)+1
print(freq)
for j in range(3):
    if j in freq:
        for a in range(freq[j]):
            print(j," ")
