#Leetcode 63
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #return math.comb(m+n-2,m-1)
        N=m+n-2
        r=min(m-1,n-1)
        count=1
        for i in range(1,r+1):
            count=count*(N-r+i)//i
        return count
