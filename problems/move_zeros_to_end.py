

nums = [1, 3, 0, 0, 4, 5, 0, 6, 2, 0, 4]


# move zeros to end
# j = 0
# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[i], nums[j] = nums[j], nums[i] 
#         j += 1


# move zeros to beginning
j = len(nums)-1
for i in range(len(nums)-1, -1, -1):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j -= 1





print(nums)