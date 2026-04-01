def singleNumber(nums):
    xor = 0
    for i in nums:
        xor = xor ^ i
    return xor
nums=[2, 3, 2, 4, 4]
print(singleNumber(nums))