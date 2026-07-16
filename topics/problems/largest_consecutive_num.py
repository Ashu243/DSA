nums = [100,4,200,1,3,2, 1]

# def largest_consc(nums):
#     n = len(nums)
#     count = 0
#     max_count = 0
#     num = 0
#     for i in range(n):
#         num = nums[i]
#         count = 1
#         while num+1 in nums:
#             count += 1
#             num += 1
#         if count> max_count:
#             max_count = count
#         count = 0
    
#     return max_count


# print(largest_consc(nums))

 

# def largest_consec_better(nums):
#     nums.sort()
#     n = len(nums)
#     smallest_num = float('-inf')
#     count = 0
#     max_count = 0

#     for i in range(n):
#         if nums[i]-1 == smallest_num:
#             count += 1
#             smallest_num = nums[i]
#             if count > max_count:
#                 max_count = count
#         elif nums[i]!= smallest_num: 
#             count = 1
#             smallest_num = nums[i]

#     return max_count
            

# print(largest_consec_better(nums))





def largest_consec_optimal(nums):
    my_set = set(nums)
    max_count = 0
    
    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            
            while x + 1 in my_set:
                x += 1
                count += 1
            
            max_count = max(max_count, count)
    
    return max_count
        
print(largest_consec_optimal(nums))

