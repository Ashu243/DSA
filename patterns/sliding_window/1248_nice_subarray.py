nums = [1,1,2,1,1]
k = 3


def nice_subarray(nums, k):
    prefix_sum = 0
    numsDict = {0:1}
    result = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 0:
            nums[right] = 0
        else:
            nums[right] = 1
        
        prefix_sum += nums[right]

        ans = prefix_sum - k
        if ans in numsDict:
            result += numsDict[ans]
        
        numsDict[prefix_sum] = numsDict.get(prefix_sum, 0) + 1
    
    return result

print(nice_subarray(nums, k))

