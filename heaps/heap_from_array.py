arr = [1, 8, 7, 16, 11, 12, 2, 4]

def heap_from_arr(arr):
    n = len(arr)

    def heapify_down(arr, index):
        largestidx = index
        leftidx = (2*index)+1
        rightidx = (2*index)+2

        if leftidx < n and arr[leftidx] > arr[index]:
            largestidx = leftidx
        if rightidx < n and arr[rightidx] > arr[largestidx]:
            largestidx = rightidx
        
        if largestidx != index:
            arr[largestidx], arr[index] = arr[index], arr[largestidx]
            heapify_down(arr, largestidx)

    for i in range(n // 2, -1, -1):
        heapify_down(arr, i)
    
    return arr

print(heap_from_arr(arr))

