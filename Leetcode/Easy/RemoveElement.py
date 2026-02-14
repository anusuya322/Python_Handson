class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lt=0
        rt=len(nums)
        while lt<rt:
            if nums[lt]==val:
                nums[lt]=nums[rt-1]
                rt=rt-1
            else:
                lt=lt+1
        return rt