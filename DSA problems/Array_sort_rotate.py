nums = [3,4,5,1,2]

def arr_rotate_sort(nums):
    n = len(nums)
    k = 0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            k += 1

    if k > 1:
        return False    
    else:
        return True


print(arr_rotate_sort(nums))            