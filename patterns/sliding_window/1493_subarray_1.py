nums = [0,1,1,1,0,1,1,0,1]


def longestSubarray(nums):
    left = 0
    maxlen = 0
    zeroPosition = float('-inf')

    for right in range(len(nums)):
        if nums[right]==0:
            if zeroPosition >= 0:
                left = zeroPosition+1
            zeroPosition = right
    
        maxlen = max(maxlen, right-left+1)
    
    return maxlen-1

print(longestSubarray(nums))