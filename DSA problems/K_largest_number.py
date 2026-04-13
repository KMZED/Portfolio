a = [3,4,1,2,5,6]
k = 2

def k_largest(nums,k):
    return sorted(nums, reverse = True)[k-1]

print(k_largest(a,k))