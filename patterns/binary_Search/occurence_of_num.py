nums = [9, 9, 10, 10, 10, 10, 14, 15]
target = 10

def count_the_occurence(nums, target):
    left = 0
    right = len(nums)-1
    first_occ = -1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] >= target:
            if nums[mid] == target:
                first_occ = mid
            right = mid -1
        else:
            left = mid+1

    left = 0
    right = len(nums)-1
    last_occ = -1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] <= target:
            if nums[mid] == target:
                last_occ = mid
            left = mid+1
        else:
            right = mid -1
    
    return last_occ - first_occ + 1


print(count_the_occurence(nums, target))
