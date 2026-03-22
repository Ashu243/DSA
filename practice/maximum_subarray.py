nums = [-2,1,-3,4,-1,2,1,-5,4]

# brute force
# total_sum = 0
# max_total_sum = float('-inf')
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         total_sum = total_sum + nums[j]
#         if total_sum>max_total_sum:
#             max_total_sum = total_sum
#     total_sum = 0

# print(max_total_sum)

# optimal solution

total_sum = 0
largest_total_sum = 0
for i in range(len(nums)):
    total_sum = total_sum + nums[i]
    if total_sum<0:
        total_sum = 0
    if total_sum>largest_total_sum:
        largest_total_sum = total_sum

print(largest_total_sum)