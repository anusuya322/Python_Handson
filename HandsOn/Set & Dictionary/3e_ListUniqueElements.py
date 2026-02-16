n=int(input("Enter the list size:"))
li=[]
print("Enter the list elements: ")
for i in range(n):
    li.append(input())
unique_list=list(set(li))
print(unique_list)