n1=int(input("enter dict1 size:"))
n2=int(input("Enter dict2 size:"))
d1={}
d2={}
for _ in range(n1):
    key=int(input("Enter Key:"))
    value=int(input("Enter Value:"))
    d1[key]=value
for _ in range(n2):
    key=int(input("Enter Key:"))
    value=int(input("Enter Value"))
    d2[key]=value
d3={}
for key in d1.keys() | d2.keys():
    d3[key]=d1.get(key,0)+d2.get(key,0)
print(d3)
