nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]



# bruteforce way
# def max_subarray_sum(nums):
#     n = len(nums)
#     sum = 0 
#     max_sum = float('-inf')
#     for i in range(n):
#         for j in range(i, n):
#             sum = sum + nums[j]
#             if sum > max_sum:
#                 max_sum = sum
#         sum = 0
    
#     return [sum, max_sum]

# print(max_subarray_sum(nums))

# optimal way

def max_subarray_sum(nums):
    n = len(nums)
    total = 0
    max_total = float('-inf')
    for i in range(n):
        total = total + nums[i]
        if total > max_total:
            max_total = total
        if total < 0:
            total = 0

    return max_total

print(max_subarray_sum(nums))