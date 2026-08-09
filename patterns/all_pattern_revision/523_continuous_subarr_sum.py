nums = [23,2,4,6,7]
k = 6

def continuous_subarr_sum(nums, k):
    prefix_sum = 0
    numsdict = {0: 1}

    for i in range(len(nums)):
        prefix_sum += nums[i]
        ans = prefix_sum % k
        if ans in numsdict:
            if i - numsdict[ans] >= 2:
                return True
        else:
            numsdict[ans] = i
    
    return False

print(continuous_subarr_sum(nums, k))