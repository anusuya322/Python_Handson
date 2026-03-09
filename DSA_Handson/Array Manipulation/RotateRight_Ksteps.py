n=int(input("Enter the array size:"))
li=[]
for _ in range(n):
    li.append(int(input()))
k=int(input("Enter the no of steps:"))
k=k%n
for i in range(0,k):
   temp=li[n-1]
   for j in range(n-1,0,-1):
      li[j]=li[j-1]
   li[0]=temp
print(li)