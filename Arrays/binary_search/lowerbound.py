nums = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7]
target = 4

def lower_bound(nums, target):
    left = 0
    right = len(nums)-1
    result = -1

    while left<=right:
        mid = (left+right) // 2
        if nums[mid]>= target:
            result = mid
            right = mid-1
        else:
            left = mid+1
    return result

print(lower_bound(nums, target))