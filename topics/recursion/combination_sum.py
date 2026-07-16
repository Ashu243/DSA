nums = [2,3,6,7]
target = 7

def combination_sum(nums, target):
    result = []

    def backtrack(index, current, total, result, target):
        if total == target:
            result.append(current.copy())
            return
        if index >= len(nums):
            return
        if total > target:
            return
        current.append(nums[index])
        sum = total + nums[index]
        backtrack(index, current, sum, result, target)
        current.pop()
        sum = total
        backtrack(index+1, current, sum, result, target)


    backtrack(0, [], 0, result, target)
    return result

print(combination_sum(nums, target))
