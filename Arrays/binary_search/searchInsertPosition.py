nums = [1,3,5,6]
target = 7


def search_insert_position(nums, target):
    right = len(nums) - 1
    left = 0
    ans = -1
    if (target>nums[-1]):
        return right+1
    while left<=right:
        mid = (left+right) // 2
        if nums[mid] == target:
            ans = mid
            break
        elif nums[mid]> target:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans

print(search_insert_position(nums, target))
        