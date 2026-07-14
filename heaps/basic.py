# heapify algorithm
import math

# arr = [12, 10, 9, 6, 8, 5, 7, 2]
arr2 = [2, 7, 5, 8, 6, 9, 10, 12]
val = 1
index = 7


def heapify(arr, val, index):
    n = len(arr)


    def heapify_down(arr, index):
        smallestidx = index
        leftidx = (2*index)+1
        rightidx = (2*index)+2

        if leftidx < n and arr[leftidx] < arr[index]:
            smallestidx = leftidx
        if rightidx < n and arr[rightidx] < arr[smallestidx]:
            smallestidx = rightidx
        
        if smallestidx != index:
            arr[smallestidx], arr[index] = arr[index], arr[smallestidx]
            heapify_down(arr, smallestidx)


    def heapify_up(arr, index):
        up_idx = (index-1) // 2
        print(up_idx)

        if up_idx > -1 and arr[up_idx] > arr[index]:
            arr[index], arr[up_idx] = arr[up_idx], arr[index]
            index = up_idx
            heapify_up(arr, index)


    if arr[index] > val:
        arr[index] = val
        heapify_up(arr, index)
    else:
        arr[index] = val
        heapify_down(arr, index)
    
    return arr

print(heapify(arr2, val, index))