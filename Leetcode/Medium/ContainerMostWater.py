class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        lt=0
        rt=len(height)-1
        while(lt<rt):
            width=rt-lt
            ht=min(height[rt],height[lt])
            area=width*ht
            ans=max(area,ans)
            if(height[lt]<height[rt]):
                lt+=1
            else:
                rt-=1
        return ans