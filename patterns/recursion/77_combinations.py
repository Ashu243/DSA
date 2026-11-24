n = 4
k = 2

def combinations(n, k):
    result = []
    nums = [x for x in range(1, n+1)]

    def recursion(index, arr):
        if len(arr) == k:
            result.append(arr.copy())
            return
        if index > n-1:
            return
        
        arr.append(nums[index])
        index+=1
        recursion(index, arr)
        arr.pop()
        recursion(index, arr)
    
    recursion(0, [])
    return result


print(combinations(n ,k))