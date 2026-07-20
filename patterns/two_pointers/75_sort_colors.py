nums = [1,0,2]


# brute force
# def sort_colors(nums):
#     zerocount = 0
#     onecount = 0
#     twocount = 0

#     for i in range(len(nums)):
#         if nums[i] == 0:
#             zerocount += 1
#         elif nums[i] == 1:
#             onecount += 1
#         else:
#             twocount += 1
    
#     def helper(starting, end, value):
#         for i in range(starting, end):
#             nums[i] = value

#     print(zerocount, onecount, twocount)
    
#     helper(0, zerocount, 0)
#     helper(zerocount, (onecount+zerocount), 1)
#     helper((onecount+zerocount), (zerocount+onecount+twocount), 2)
    
#     return nums

# print(sort_colors(nums))


def sort_colors(nums):
    left = 0
    mid = 0
    right = len(nums)-1

    while mid<= right:
        if nums[mid] == 2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
        if nums[mid] == 0:
            nums[mid], nums[left] = nums[left], nums[mid]
            mid += 1
            left += 1
        else:
            mid += 1
        
    return nums

print(sort_colors(nums))