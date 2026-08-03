def findMiddleIndex(self, nums) -> int:
    left = 0
    total_sum = sum(nums)
    for i in range(len(nums)):
        right = total_sum - left -nums[i]
        if left == right:
            return i
        left += nums[i]
    return -1