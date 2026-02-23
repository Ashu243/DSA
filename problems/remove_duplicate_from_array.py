nums = [-1, 0, 0, 1, 1, 3, 3, 4, 4 , 5, 5, 5, 9]

# freq_map = {}
# def removeDuplicates(nums):

#     for i in range(len(nums)):
#         freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

#     j = 0
#     for i in freq_map:
#         nums[j] = i
#         j += 1
    
#     return j


# print(removeDuplicates(nums))
# print(nums)


# optimal solution

def removeDuplicates(nums):
    i=0
    j=1

    for k in range(len(nums)-1):
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

        j +=1
    return i+1

print(removeDuplicates(nums))
print(nums)