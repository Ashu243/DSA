my_dict = {}
nums = [1, 5, 2, 6, 1, 6, 3, 7, 3, 8, 15, 74]

# for i in range(len(nums)):
#     if nums[i] in my_dict:
#         # my_dict[nums[i]] = my_dict.get(nums[i])+1
#         my_dict[nums[i]] += 1
#     else:
#         my_dict[nums[i]] = 1 

# print(my_dict)

for i in range(len(nums)):
    my_dict[nums[i]] = my_dict.get(nums[i], 0) + 1

print(my_dict)