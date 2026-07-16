nums = [10, 5, 10, 8, 7]

largest = nums[0]
second_largest = float('-inf')

for i in range(len(nums)):
    if nums[i]>largest:
        largest = nums[i]
    if nums[i]<largest and nums[i]>second_largest:
        second_largest = nums[i]

print(second_largest)