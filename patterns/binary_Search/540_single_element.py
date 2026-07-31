nums = [1,1,2,3,3,4,4,8,8]

def single_element(nums):
    left = 0
    right = len(nums)-1
    if right == 0:
        return nums[0]

    while left < right:
        mid = (left+right) // 2
        if mid%2 == 1 and nums[mid] == nums[mid-1] or mid%2==0 and nums[mid] == nums[mid+1]:
            left = mid+1
        else:
            right = mid
    return nums[left]

print(single_element(nums))
        
