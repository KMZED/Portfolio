nums = [0,1,0,3,12]

def moveZeroes(nums):
   left = 0 # pointer for non-zero elements
   for n in range(len(nums)):
       if nums[n] != 0:
           nums[left], nums[n] = nums[n], nums[left] # swap non-zero element to the left
           left += 1

moveZeroes(nums)
print(nums)