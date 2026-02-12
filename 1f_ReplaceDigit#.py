string=input("Enter a string: ")
arr=list(string)
res=""
for i in arr:
    if i.isdigit():
        res+="#"
    else:
        res+=i
print("The resultant string for ",string,"is :",res)


