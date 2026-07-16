nums = [-1, 0, 1, 2, -1, -4]

# def three_sum(nums):
#     n = len(nums)
#     my_set = set()

#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if nums[i]+nums[j]+nums[k] == 0:
#                     temp = [nums[i],nums[j],nums[k]]
#                     temp.sort()
#                     my_set.add(tuple(temp))
    
#     return [tuple(ans) for ans in my_set()]

# print(three_sum(nums))

# def three_sum_better(nums):
#     n = len(nums)
#     my_set = set()

#     for i in range(n):
#         fresh_set = set()
#         for j in range(i+1, n):
#             k = -(nums[i]+nums[j])
#             if k in fresh_set:
#                 temp = [nums[i], nums[j], k]
#                 temp.sort()
#                 my_set.add(tuple(temp))
#             fresh_set.add(nums[j])

#     return [list(ans) for ans in my_set]

# print(three_sum_better(nums))



def three_sum_optimal(nums):
    n = len(nums)
    arr = []
    nums.sort()
    for i in range(n):
        if i!=0 and nums[i] == nums[i-1]:
            continue

        j = i+1
        k = n-1
        while j<k:
            sum = nums[i]+nums[j]+nums[k]
            if sum<0:
                j+=1
            elif sum>0:
                k-=1
            else:
                temp = [nums[i], nums[j], nums[k]]
                arr.append(temp)
                j+= 1
                k-=1
                while j<k and nums[j] == nums[j-1]:
                    j+=1
                while k>j and nums[k] == nums[k+1]:
                    k-=1

    return arr

print(three_sum_optimal(nums))


