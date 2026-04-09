A = [3,4,2,1]

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break


insertionSort(A)
print("Sorted array is:", A)