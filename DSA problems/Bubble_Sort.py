A = [3,4,2,1]

def bubbleSort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True

bubbleSort(A)
print("Sorted array is:", A)