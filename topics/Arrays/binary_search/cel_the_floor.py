nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14]
target = 2

def ceil_the_floor(nums, target):
    right = len(nums)-1
    left = 0
    floor = -1
    ceil = -1
    while left<=right:
        mid = (left+right)//2
        if nums[mid]==target:
            floor = target
            ceil = target
            break
        elif nums[mid]> target:
            right = mid-1
            ceil = nums[mid]
        else:
            floor = nums[mid]
            left = mid+1
    return [floor, ceil]

print(ceil_the_floor(nums, target))