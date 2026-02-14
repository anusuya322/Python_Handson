n=int(input("Enter the size of list:"))
li=[]
for i in range(n):
    num=int(input())
    li.append(num)
even=[]
for i in range(n):
    if li[i]%2==0:
        even.append(li[i]*li[i])
print("Squares of even numbers:",even)