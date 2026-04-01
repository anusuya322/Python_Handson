def runningSum(nums):
        total = 0
        ans = []
        for i in nums:
            total += i
            ans.append(total)
        return ans
nums=list(map(int, input().split()))
print(runningSum(nums))