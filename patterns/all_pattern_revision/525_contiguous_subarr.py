nums = [0,1,1,1,1,1,0,0,0]

def contiguous_subarr(nums):
    prefix_sum = 0
    numsdict = {0:-1}
    maxlen = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1
        if prefix_sum in numsdict:
            maxlen = max(maxlen, i-numsdict[prefix_sum])
        else:
            numsdict[prefix_sum] = i
    return maxlen

print(contiguous_subarr(nums))

