# nums = [2,4,6]
# target = 6
# def subsequences(nums, target):
#     result = []
#     def helper(index, current):
#         if len(nums) == index:
#             if sum(current) == target:
#                 result.append(current.copy())
#             return
#         current.append(nums[index])
#         helper(index+1, current)

#         current.pop()
#         helper(index+1, current)
#     helper(0, [])
#     return result

# print(subsequences(nums, target))


nums = [2,4,6]
target = 6
def subsequences(nums, target):
    result = []
    def helper(index, current, sum):
        if sum == target:
            result.append(current.copy())
            return
        elif sum> target:
            return
        elif len(nums) <= index:
            return
        current.append(nums[index])
        total = (sum + nums[index])
        helper(index+1, current, total)

        elem = current.pop()
        total = total - elem
        helper(index+1, current, total)
    helper(0, [], 0)
    return result

print(subsequences(nums, target))