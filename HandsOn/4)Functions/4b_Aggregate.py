def aggregate(*nums,op="sum"):
    if not nums:
        return None
    if op=="sum":
        return sum(nums)
    elif op=="avg":
        return sum(nums)/len(nums)
    elif op=="max":
        return max(nums)
    else:
        return None
n=int(input())
li=[]
print("Enter the list elements:")
for _ in range(n):
    li.append(int(input()))
op=input("Enter the operation:")
ans=aggregate(*li,op=op)
print("The",op,"is ",ans)
