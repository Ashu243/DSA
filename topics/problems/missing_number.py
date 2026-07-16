nums = [0, 1, 4, 2, 3]
# def find_missing_num(nums):
#     n = len(nums)

#     for i in range(n+1):
#         nums2[i] = 0
    
#     for num in nums:
#         nums2[num] = 1

#     for k,v in nums2.items():
#         if v == 0:
#             return k

# answer = find_missing_num(nums)
# print(answer)

def find_missing_num2(nums):
    totalsum = 0
    actualsum = 0
    for i in range(len(nums)+1):
        totalsum = totalsum + i
    
    for num in nums:
        actualsum = actualsum + num

    return totalsum - actualsum

print(find_missing_num2(nums))