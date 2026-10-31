nums = [0,0,1,1,1,1,2,3,3]


def remove_duplicates(nums):
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1
        else:
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
    
    return left+1

print(remove_duplicates(nums))
            