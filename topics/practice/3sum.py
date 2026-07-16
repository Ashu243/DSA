nums = [-1,0,1,2,-1,-4]

# def three_sum_brute(nums):
#     n = len(nums)
#     my_set = set()
#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if nums[i]+nums[j]+nums[k] == 0:
#                     temp = [nums[i], nums[j], nums[k]]
#                     temp.sort()
#                     my_set.add(tuple(temp))
    
#     return [list(ans) for ans in my_set]


# print(three_sum_brute(nums))

def three_sum_better(nums):
    n = len(nums)
    my_set = set()
    for i in range(n):
        freshSet = set()
        for j in range(i+1, n):
            k = -(nums[i]+nums[j])
            if k in freshSet:
                temp = [nums[i], nums[j], k]
                temp.sort()
                my_set.add(tuple(temp))
            freshSet.add(nums[j])
    return [list(ans) for ans in my_set]

print(three_sum_better(nums))
