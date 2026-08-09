nums = [4,5,0,-2,-3,1]
k = 5

def subarraysDivByK(nums, k):
    prefix_sum = 0
    numsdict = {0:1}
    result = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        ans = prefix_sum % k
        if ans in numsdict:
            result += numsdict[ans]
        
        numsdict[ans] = numsdict.get(ans, 0) + 1
    return result

print(subarraysDivByK(nums, k))
