n=int(input("Enter a number:"))
count=0
for i in range(1,n):
    if n%i==0:
        count+=1
print(count)