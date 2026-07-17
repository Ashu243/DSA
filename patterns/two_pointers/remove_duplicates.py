
nums = [0,0,1,1,1,2,2,3,3,4]


def remove_duplicates(nums):
    i, j = 0, 1

    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1

    return i+1

print(remove_duplicates(nums))