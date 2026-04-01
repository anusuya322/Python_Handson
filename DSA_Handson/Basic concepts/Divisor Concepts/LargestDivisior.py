n=int(input("Enter a number:"))
minimum=1
for i in range(1,n//2+1):
    if n%i==0:
        minimum=i
        #print(minimum)
print(minimum)
'''for i in range(n//2,0,-1):
    if n%i==0:
        print(i)
        break'''