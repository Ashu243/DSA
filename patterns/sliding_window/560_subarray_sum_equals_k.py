nums = [1]
k = 0


def subarraySum(nums, k):
    n = len(nums)
    prefix_sum = 0
    
    numsdict = {}
    result = 0

    for right in range(n):
        prefix_sum += nums[right]
        if prefix_sum == k:
            result += 1

        ans = prefix_sum - k
        if ans in numsdict:
            result += numsdict[ans]

        numsdict[prefix_sum] = numsdict.get(prefix_sum, 0) + 1
    
    return result

print(subarraySum(nums, k))