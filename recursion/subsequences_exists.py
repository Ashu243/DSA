# nums = [3, 5, 7 ,8, 6]
# k = 9
# def subsequence_exists(nums, k):
#     is_exists = False
#     def backtracking(index, total, current):
#         nonlocal is_exists
#         if total == k:
#             is_exists = True
#             return
#         elif len(nums) == index:
#             return
        
#         current.append(nums[index])
#         total = total + nums[index]
#         backtracking(index+1, total, current)

#         elem = current.pop()
#         total = total - elem
#         backtracking(index+1, total, current)
    
#     backtracking(0, 0, [])
#     return is_exists
# print(subsequence_exists(nums, k))



nums = [3, 5, 7 ,4, 6]
k = 9
def subsequence_exists(nums, k):
    count = 0
    def backtracking(index, total, current):
        nonlocal count
        if total == k:
            count += 1
            return
        elif total>k:
            return
        elif len(nums) == index:
            return
        
        current.append(nums[index])
        total = total + nums[index]
        backtracking(index+1, total, current)

        elem = current.pop()
        total = total - elem
        backtracking(index+1, total, current)
    
    backtracking(0, 0, [])
    return count
print(subsequence_exists(nums, k))