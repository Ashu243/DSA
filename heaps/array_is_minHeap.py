
arr = [4, 6, 9, 12, 16, 13 ,19, 21]

def is_arr_minHeap(arr):
    if len(arr) == 0:
        return True
    n = len(arr)
    for i in range(n//2):
        leftchild = (2*i) + 1
        rightchild = (2*i) + 2

        if leftchild < n and arr[leftchild] < arr[i]:
            return False
        if rightchild <n and arr[rightchild] < arr[i]:
            return False
    
    return True

print(is_arr_minHeap(arr))
