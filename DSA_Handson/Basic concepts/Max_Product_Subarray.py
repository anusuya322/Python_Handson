def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        temp = max(num, num * max_prod, num * min_prod)
        min_prod = min(num, num * max_prod, num * min_prod)
        max_prod = temp
        result = max(result, max_prod)
    return result
print(maxProduct([2,3,-2,4]))