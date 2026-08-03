nums = [0,1,1,1,1,1,0,0,0]


def contiguous_array(nums):
    n = len(nums)
    numsdict = {0:-1}
    total_sum = 0
    maxlen = 0

    for i in range(n):
        if nums[i] == 0:
            total_sum -= 1
        else:
            total_sum += 1

        if total_sum in numsdict:
            maxlen = max(maxlen, i - numsdict[total_sum])
        else:
            numsdict[total_sum] = i
    return maxlen

print(contiguous_array(nums))
