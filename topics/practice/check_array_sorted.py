nums = [1, 2, 2, 3, 4]

j = 1
is_sorted = True
for i in range(len(nums)-1):
    if nums[j] < nums[i]:
        is_sorted = False
        break
    j += 1
print(is_sorted)