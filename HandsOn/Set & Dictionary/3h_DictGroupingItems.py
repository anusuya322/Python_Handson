n=int(input("Enter the number of items:"))
data=[]
for _ in range(n):
    item=input("enter the item:")
    category=input("Enter the category:")
    data.append((item,category))
print(data)
d={}
for item,category in data:
    if category not in d:
        d[category]=[]
    d[category].append(item)
print(d)