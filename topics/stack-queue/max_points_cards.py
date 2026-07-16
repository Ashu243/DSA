nums = [9,7,7,9,7,7,9]
k = 7


def max_points(nums, k):
    n = len(nums)
    if n == k:
        return sum(nums)
    i, j= 0, n-1
    leftsum = 0
    rightsum = 0
    maximum = 0

    while i<k:
        leftsum = leftsum + nums[i]
        i += 1
    
    i -= 1
    maximum = max(maximum, leftsum)
    
    while i>=0:
        leftsum = leftsum - nums[i]
        rightsum = rightsum + nums[j]
        maximum = max(maximum, leftsum+rightsum)
        i -= 1
        j -= 1

    return maximum

print(max_points(nums, k))