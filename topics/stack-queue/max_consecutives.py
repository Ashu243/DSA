nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3


def max_consecutive_ones(nums, k):
    zero_count = 0
    left = 0
    maximum = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        maximum = max(maximum, right-left+1)

    return maximum


print(max_consecutive_ones(nums, k))

