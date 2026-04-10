A = [3,4,2,1]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]
    l = [x for x in arr[:-1] if x <= p]
    r = [x for x in arr[:-1] if x > p]
    
    l = quick_sort(l)
    r = quick_sort(r)

    return l + [p] + r

A = quick_sort(A)
print("Sorted array is:", A)