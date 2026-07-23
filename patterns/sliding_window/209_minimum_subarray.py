target = 7
nums = [2,3,1,2,4,3]

def minSubArrayLen(target, nums):
    left = 0
    total_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total_sum += nums[right]

        if total_sum >= target:
            while total_sum >= target:
                min_len = min(min_len, right-left+1)
                total_sum -= nums[left]
                left += 1

    return min_len if min_len != float('inf') else 0

print(minSubArrayLen(target, nums))

