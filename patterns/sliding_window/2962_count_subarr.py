nums = [1,3,2,3,3]
k = 2

def countSubarr(nums, k):
    left = 0
    total_count = 0
    n = len(nums)

    maxNum = max(nums)
    maxFreq = 0

    for right in range(n):
        if nums[right] == maxNum:
            maxFreq += 1
        
        while maxFreq == k:
            total_count += n-right
            if nums[left] == maxNum:
                maxFreq -= 1
            left += 1
    
    return total_count

print(countSubarr(nums, k))