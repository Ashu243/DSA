nums = [2,2,2,1,2,2,1,2,2,2]
k = 2


def niceSubarrays(nums, k):
    prefix_sum = 0
    numsdict = {0: 1}
    result = 0

    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            prefix_sum += 1
        
        ans = prefix_sum - k
        if ans in numsdict:
            result += numsdict[ans]
        numsdict[prefix_sum] = numsdict.get(prefix_sum, 0) + 1
    
    return result
print(niceSubarrays(nums, k))

