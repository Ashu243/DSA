nums = [1,2,3]
k = 3

def subarr_sum(nums, k):
    prefix_sum = 0
    numsdict = {}
    result = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum == k:
            result += 1
        ans = prefix_sum - k
        if ans in numsdict:
            result += numsdict[ans]
        numsdict[prefix_sum] = numsdict.get(prefix_sum, 0)+1
    
    return result

print(subarr_sum(nums, k))