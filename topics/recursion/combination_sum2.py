candidates = [2,5,2,1,2]
target = 5


def combination_sum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(index, current, total):
        if total == target:
            result.append(current.copy())
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates [i-1]:
                continue

            if total>target:
                break

            current.append(candidates[i])
            backtrack(i+1, current, total + candidates[i])

            current.pop()
        
    backtrack(0, [], 0)
    return result

print(combination_sum2(candidates, target))
