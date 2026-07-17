nums = [-7,-3,2,3,11]

def sq_sorted_array(nums):
    left = 0
    n = len(nums)
    right = n-1
    write = n-1
    result = [0]*n

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[write] = nums[left]**2
            left += 1
        else:
            result[write] = nums[right]**2
            right -= 1
        write -= 1
    
    return result




print(sq_sorted_array(nums))
    
