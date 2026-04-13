from functools import cmp_to_key
A = [3,30,34,5,9]

def largest_sum(nums):
    nums = list(map(str,nums))

    def compare(a,b):
        if a+b > b+a:
            return -1
        else:
            return 1


    nums.sort(key = cmp_to_key(compare))
    results = ''.join(nums)

    return '0' if results[0] == '0' else results

print(largest_sum(A))                