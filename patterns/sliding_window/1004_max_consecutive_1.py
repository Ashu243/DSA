nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

def max_consec_ones(nums, k):
    left = 0
    zerocount = 0
    max_ones = 0


    for right in range(len(nums)):
        if nums[right] == 0:
            zerocount += 1

        while zerocount > k:
            if nums[left] == 0:
                zerocount -= 1
            left += 1
        
        max_ones = max(max_ones, right-left+1)
    return max_ones

print(max_consec_ones(nums, k))
