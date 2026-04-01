def isPowerOfTwo(n):
        if n==1:
            return True
        elif(n>0 and (n&(n-1))==0):
            return True
        return False
n=int(input())
print(isPowerOfTwo(n))