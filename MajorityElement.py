nums = [3,2,3]

def majorityElement(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, freq in count.items(): 
        if freq > len(nums) // 2:
            return num   

print(majorityElement(nums))