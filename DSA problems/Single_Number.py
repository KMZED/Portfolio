# LeetCode 136 - Single Number
nums = [4, 1, 2, 1, 2]

def singleNumber(nums):
    result = 0
    for n in nums:  # XOR cancels out duplicates
        result ^= n
    return result

result = singleNumber(nums)
print(result)
