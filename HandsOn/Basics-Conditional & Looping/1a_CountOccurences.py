str=input("Enter the string:")
substr=input("Enter the substring:")
count=0
for i in range(len(str)-len(substr)+1):
    if str[i:i+len(substr)]==substr:
        count+=1
print("The number of occurrences of ",substr,"in ",str,"is ",count)