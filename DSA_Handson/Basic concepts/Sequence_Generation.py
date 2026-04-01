def sequenceGeneration(n):
    arr=[]
    for i in range(1,n+1):
        if i%2==1:
            arr.append((i+1)//2)
        else:
            arr.append(-(i//2))
    return arr
n=int(input())
print(sequenceGeneration(n))
