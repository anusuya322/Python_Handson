def make_counter(start=0):
    count=start
    def counter():
        nonlocal count
        count+=1
        return count
    return counter
start=(int(input("Enter start value:")))
time=int(input("Enter how many times to call:"))
ans=make_counter(start)
print("Output:")
for _ in range(time):
    print(ans())