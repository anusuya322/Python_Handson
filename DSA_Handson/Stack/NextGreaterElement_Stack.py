def nextGreaterElements(nums):
    st = []
    res = [-1] * len(nums)
    n = len(nums)
    for i in range(2 * n):
        while st and nums[i % n] > nums[st[-1]]:
            res[st.pop()] = nums[i % n]
        if i < n:
            st.append(i)
    return res
nums = [1, 2, 1]
result = nextGreaterElements(nums)
print(result)
