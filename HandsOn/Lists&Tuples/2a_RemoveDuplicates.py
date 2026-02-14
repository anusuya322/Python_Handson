n=int(input("Enter the size:"))
li=[]
for i in range(n):
    ele=int(input())
    li.append(ele)
seen=set()
result=[]
for num in reversed(li):
    if num not in seen:
        result.append(num)
        seen.add(num)
result.reverse()
print(result)



