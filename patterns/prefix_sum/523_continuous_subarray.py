nums = [5,0,0,0]
k = 3

def checkSubarraySum(nums, k):
    if len(nums) < 2:
        return False
    prefixsum = 0
    numsdict = {0: -1}
    for i in range(len(nums)):
        prefixsum += nums[i]
        ans = prefixsum % k
        if ans in numsdict: 
            if i - numsdict[ans] >= 2:
                return True
        else:
            numsdict[ans] = i
    
    return False
print(checkSubarraySum(nums, k))