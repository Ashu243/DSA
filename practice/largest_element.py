nums = [3, 7, 2, 9, 5]

largest = nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        largest = nums[i]

print(largest)