nums = [1,2,3]


def subset(nums):
    result = []
    n = len(nums)

    def recursion(index, arr):
        if index >= n:
            result.append(arr.copy())
            return
        
        arr.append(nums[index])
        recursion(index+1, arr)
        arr.pop()
        recursion(index+1, arr)
    recursion(0, [])
    return result

print(subset(nums))