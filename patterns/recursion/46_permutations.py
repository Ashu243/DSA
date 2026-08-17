nums = [1,2,3]

def permutations(nums):
    result = []

    def backtrack(arr):
        if len(arr) == len(nums):
            result.append(arr.copy())
            return 
        for x in nums:
            if x not in arr:
                arr.append(x)
                backtrack(arr)
                arr.pop()
    backtrack([])
    return result

print(permutations(nums))