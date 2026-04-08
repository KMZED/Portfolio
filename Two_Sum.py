array = [2, 7, 11, 15]
target = 9  

def two_sum(nums, target):
    index = {} 
    for i, num in enumerate(nums): 
        remainder = target - num 
        if remainder in index: 
            return (index[remainder], i)
        index[num] = i

result = two_sum(array, target)
print(result)
      