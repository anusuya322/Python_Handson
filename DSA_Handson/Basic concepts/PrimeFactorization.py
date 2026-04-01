def primeFactorization(n):
    i=2
    while i*i<=n:
        while n%i==0:
            print(i,end=" * ")
            n//=i
        i+=1
    if n>1:
        print(n)
n=int(input())
primeFactorization(n)
'''def countPrimes(n):
        if n <= 2:
            return 0
        # count=0
        prime = [True] * n
        prime[0] = prime[1] = False
        i = 2
        while i * i < n:
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
            i += 1
        return sum(prime)
n=int(input())
print(countPrimes(n))'''

