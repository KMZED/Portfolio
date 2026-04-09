A = [3,4,2,1]
def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(arr)
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

insertionSort(A)
print("Sorted array is:", A)