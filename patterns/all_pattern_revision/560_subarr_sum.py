nums = [1,1,1]
k = 2

def subarr_sum(nums, k):
    prefix_sum = 0
    numsdict = {0: 1}
    result = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum - k in numsdict:
            result += numsdict[prefix_sum - k]
        numsdict[prefix_sum] = numsdict.get(prefix_sum, 0) + 1
    return result

print(subarr_sum(nums, k))