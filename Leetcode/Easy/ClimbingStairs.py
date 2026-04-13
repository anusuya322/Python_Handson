class Solution:
    def climbStairs(self, n: int) -> int:
        #def fib(n):
        if n==1:
            return 1
        if n==2:
            return 2
        a,b=0,1
        for _ in range(1,n+1):
            a,b=b,a+b
        return b