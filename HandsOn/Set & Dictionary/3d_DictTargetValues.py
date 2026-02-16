n=int(input("Enter the Dictionary size:"))
d={}
for _ in range(n):
    key=int(input())
    value=int(input())
    d[key]=value
print(d)
target=int(input("Enter the target value:"))
keys_target=[]
for key,value in d.items():
    if target==value :
        keys_target.append(key)
print(keys_target)
