n=int(input("Enter the size:"))
li=[]
for i in range(n):
    ele=int(input())
    li.append(ele)
distinct=list(set(li))
distinct.sort(reverse=True)
second_largest=distinct[1]
if len(distinct)>2:
    print(li.index(second_largest))
else:
    print("-1")
