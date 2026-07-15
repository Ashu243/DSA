import random
arr = [3,2,1,5,6,4]
k = 2

def quickselect(arr, k):
    left = 0
    right = len(arr)-1

    def partitionAndReturnIndex(left, right, pivot):
        ind = left+1
        arr[pivot], arr[left] = arr[left], arr[pivot]
        for i in range(left+1, right+1):
            if arr[i] > arr[left]:
                arr[ind], arr[i] = arr[i], arr[ind]
                ind += 1
        
        arr[left], arr[ind-1] = arr[ind-1], arr[left]
        return ind-1

    while True:
        pivot = random.randint(left, right)
        pivot = partitionAndReturnIndex(left, right, pivot)
        
        if pivot == k-1:
            return arr[pivot]
        elif pivot > k - 1:
            right = pivot - 1
        else:
            left = pivot +1



print(quickselect(arr, k))