class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        steps=0
        end=0
        farthest=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if i==end:
                end=farthest
                steps+=1
        return steps
        '''j=0
        for i in range(len(nums)):
            while j<len(nums):
                if nums[i]<nums[j]:
                    steps+=1
                j+=1
        return steps'''#compare the index..not the value