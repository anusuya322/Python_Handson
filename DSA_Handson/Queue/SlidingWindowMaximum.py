from collections import deque
def maxSlidingWindow(nums,k):
    ans = []
    dq = deque()
    for i in range(len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            ans.append(nums[dq[0]])
    return ans
k=int(input())
nums=list(map(int, input().split()))
print(maxSlidingWindow(nums,k))
