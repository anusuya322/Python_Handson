n=int(input("Enter number of list elements:"))
li=[]
for _ in range(n):
    li.append(int(input()))
for num in li:
    try:
        a=num/100
        if a==0:
            raise ZeroDivisionError("Divide by 0")
        print(a)
    except ZeroDivisionError as e:
               print("Error:",e)
