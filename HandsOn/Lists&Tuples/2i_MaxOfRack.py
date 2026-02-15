n=int(input("Enter the list size:"))
li=[]
for _ in range(n):
    li.append(int(input()))
runningSum=0
ans=[]
for i in li:
    runningSum+=i
    if runningSum<=0:
        runningSum=0
    ans.append(runningSum)
print("The Running Max values are:",ans)