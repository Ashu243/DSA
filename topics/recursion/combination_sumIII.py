k = 3
n = 7

def combination_sum3(k, n):
    nums = [i for i in range(1, 10)]
    result = []

    def backtrack(index, current, total, position):
        if position == k and total == n:
            result.append(current.copy())
            return
        if position>k or total>n:
            return
        if index >= len(nums):
            return 
        
        current.append(nums[index])
        backtrack(index+1, current, total+ nums[index], position+1)
        current.pop()
        backtrack(index+1, current, total, position)

    backtrack(0, [], 0, 0)
    return result

print(combination_sum3(k, n))


