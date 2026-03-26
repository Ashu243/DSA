nums = [5, 9, 3]

def subset_sum(nums):
    result = []

    def backtrack(index, current, total):
        if index >= len(nums):
            result.append(total)
            return
        
        current.append(nums[index])
        backtrack(index+1, current, total+nums[index])

        current.pop()
        backtrack(index+1, current, total)

    backtrack(0, [], 0)
    return result

print(subset_sum(nums))