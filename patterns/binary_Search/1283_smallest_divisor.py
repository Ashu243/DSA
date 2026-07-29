import math
nums = [1,2,5,9]
threshold = 6


def smallest_divisor(nums, threshold):
    def divisor(div):
        sum = 0
        for num in nums:
            sum += math.ceil(num / div)
            if sum > threshold:
                return False
        return True

    left = 1
    right = max(nums)

    while left <= right:
        mid = (left+right) // 2

        if divisor(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left

print(smallest_divisor(nums, threshold))