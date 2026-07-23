nums = [10,5,2,6]
k = 100


def numSubarrayProductLessThanK(nums, k):
    left = 0
    product = 1
    result = 0

    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product = product//nums[left]
            left += 1
        result += right - left + 1
    return result

print(numSubarrayProductLessThanK(nums, k))
