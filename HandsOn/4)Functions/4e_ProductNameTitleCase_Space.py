n=int(input("Enter number of names:"))
li=[]
for _ in range(n):
    li.append(input("Enter product name:"))
cleaned=list(map(lambda x:x.strip().title(),li))
print(cleaned)
cleaned_Spaces=list(map(lambda x:" ".join(x.strip().split()).title(),li))
print(cleaned_Spaces)