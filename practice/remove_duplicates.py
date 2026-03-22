nums =  [1,1,2,2,3,3,4]

def duplicates_removed(nums):
    i = 0
    j = 1
    for k in range(len(nums)-1):
        if nums[j] != nums[i]:
            nums[j], nums[i+1] = nums[i+1], nums[j]
            i += 1

        j += 1
    return i+1

print(duplicates_removed(nums))
print(nums)

