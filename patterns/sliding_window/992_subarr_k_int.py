nums = [1,2,1,2,3]
k = 2

def subarraysWithKDistinct(nums, k):
    numsDict = {}
    left = 0
    result = 0
    n = len(nums)

    for right in range(n):
        numsDict[nums[right]] = numsDict.get(nums[right], 0) + 1

        while len(numsDict) == k:
            result += n-right
            numsDict[nums[left]] -= 1
            if numsDict[nums[left]] == 0:
                numsDict.pop(nums[left])
            left += 1
    
    numsDict = {}
    result2 = 0
    left = 0
    for right in range(n):
        numsDict[nums[right]] = numsDict.get(nums[right], 0) + 1

        while len(numsDict) == k+1:
            result2 += n-right
            numsDict[nums[left]] -= 1
            if numsDict[nums[left]] == 0:
                numsDict.pop(nums[left])
            left += 1
    
    return result - result2


print(subarraysWithKDistinct(nums, k))
