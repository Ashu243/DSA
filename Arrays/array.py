# finding the largest number in an array

# nums = [3, 7, 2, 9, 4, 10, 150, 11]

# largest_num = nums[0]

# for i in range(0, len(nums)):
#     if(nums[i] > largest_num):
#         largest_num = nums[i]

# print(largest_num)


# second largest number

# nums = [3, 7, 2, 9, 4, 10, 150, 140, 11 ]

# largest_num = nums[0]
# second_largest_num = nums[0]

# for num in nums:
#     if(num > largest_num):
#         largest_num = num
#     if(num<largest_num and num>second_largest_num):
#         second_largest_num = num

# print(largest_num)
# print(second_largest_num)




# n = 3438
# num = n
# reversed_num = 0

# while num > 0:
#     last_digit = num % 10
#     print(last_digit)
#     reversed_num  = (reversed_num * 10) + last_digit
#     num = num // 10
    
# print(reversed_num)

n = 239284
num = n
count = 0 

while num > 0:
    count += 1
    num = num // 10
    
print(count)

