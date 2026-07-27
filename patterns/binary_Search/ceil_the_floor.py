nums = [9, 9, 10, 11, 12, 12, 14, 15]
target = 3

def ceil_the_floor(nums, target):
    left = 0
    right = len(nums)-1
    ceil, floor = -1, -1

    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        
        if nums[mid] > target:
            ceil = nums[mid]
            right = mid-1
        
        else:
            floor = nums[mid]
            left = mid + 1

    return [floor, ceil]

print(ceil_the_floor(nums, target))