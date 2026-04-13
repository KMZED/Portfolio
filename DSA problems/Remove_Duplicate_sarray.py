nums = [0,0,1,1,1,2,2,3,3,4]

def remove_duplicate(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    return i+1


print(remove_duplicate(nums),nums)