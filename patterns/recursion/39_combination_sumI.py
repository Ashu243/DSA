candidates = [2,3,6,7]
target = 7

def combination_sum(candidates, target):
    result = []

    def backtracking(index, arr, sum):
        if sum == target:
            result.append(arr.copy())
            return
        elif sum > target:
            return
        if index >= len(candidates):
            return
        
        sum += candidates[index]
        arr.append(candidates[index])
        backtracking(index, arr, sum)
        arr.pop()
        sum = sum - candidates[index]
        backtracking(index+1, arr, sum)
    
    backtracking(0, [], 0)

    return result

print(combination_sum(candidates, target))