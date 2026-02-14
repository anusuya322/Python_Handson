n=int(input("Enter the size of list:"))
li=[]
for i in range(n):
    num=int(input())
    li.append(num)
k=int(input("Enter the shift value:"))
k=k%n
for i in range(0,k):
    temp=li[n-1]
    for j in range(n-1,0,-1):
        li[j]=li[j-1]
    li[0]=temp
print(li)

