nums = [4,5,6,7,0,1,2]
target = 8

# def search(nums, target):
#     n = len(nums)
#     for i in range(n):
#         if nums[i] == target:
#             return i
#     return -1

# print(search(nums, target))


def search(nums, target):
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid]<=nums[right]:
            if nums[mid] <= target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
        else:
            if nums[left]<= target<= nums[mid]:
                right = mid-1
            else:
                left = mid+1
    return -1

print(search(nums, target))

