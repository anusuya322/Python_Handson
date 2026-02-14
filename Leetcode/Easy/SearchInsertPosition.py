class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lt,rt=0,len(nums)-1
        while lt<=rt:
            mid=(lt+rt)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                lt=mid+1
            else:
                rt=mid-1
        return lt