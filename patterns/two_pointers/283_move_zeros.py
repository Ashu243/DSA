nums = [0,1,0,3,12]

def move_zeros(nums):
    k = 0 

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
    return nums

print(move_zeros(nums))