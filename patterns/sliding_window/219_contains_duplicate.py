nums = [1,2,3,1]
k = 3

# hashmap solution
# def contains_duplicate(nums, k):
#     num_dict = {}

#     for i in range(len(nums)):
#         if nums[i] in num_dict:
#             val = num_dict.get(nums[i])
#             if abs(i - val) <= k:
#                 return True
#         num_dict[nums[i]] = i
    
#     return False

# print(contains_duplicate(nums, k))


# sliding window solution 

def contains_duplicate(nums, k):
    window = set()
    left = 0

    for right in range(len(nums)):
        if nums[right] in window:
            return True
        
        window.add(nums[right])

        if right - left == k:
            window.remove(nums[left])
            left += 1
    return False

print(contains_duplicate(nums, k))