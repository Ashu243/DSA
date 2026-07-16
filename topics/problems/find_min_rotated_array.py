nums = [4, 5, 6, 7, 0, 1, 2]

def min_search(nums):
    right = len(nums)-1
    left = 0

    while left<right:
        mid = (left+right) // 2
        if nums[mid]>nums[right]:
            left = mid + 1
        else:
            right = mid 
    return nums[left]
    
print(min_search(nums))