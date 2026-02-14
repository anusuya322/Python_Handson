n1=int(input("Enter the size of list1:"))
n2=int(input("Enter the size of list2"))
li1=[]
li2=[]
print("Enter the list1 element:")
for _ in range(n1):
    li1.append(int(input()))
print("Enter the list2 elements:")
for _ in range(n2):
    li2.append(int(input()))
li3=[]
i=j=0
while i<n1 and j<n2:
    li3.append(li1[i])
    li3.append(li2[j])
    i+=1
    j+=1
print("The interleaved two lists are:",li3)