# heapify algorithm
import math

arr = [12, 10, 9, 6, 8, 5, 7, 2]
val = 15
index = 6


def heapify(arr, val, index):
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


    def heapify_up(arr, index):
        up_idx = (index-1) // 2
        print(up_idx)

        if up_idx > -1 and arr[up_idx] < arr[index]:
            arr[index], arr[up_idx] = arr[up_idx], arr[index]
            index = up_idx
            heapify_up(arr, index)


    if arr[index] > val:
        arr[index] = val
        heapify_down(arr, index)
    else:
        arr[index] = val
        heapify_up(arr, index)
    
    return arr

print(heapify(arr, val, index))