n = 3

# def parenthesis(n):
#     result = []

#     def backtracking(arr, openCount, closeCount):
#         if len(arr) == n*2:
#             result.append(arr)
#             return
        
#         if openCount < n:
#             backtracking(arr+'(', openCount+1, closeCount)
#         if closeCount < openCount:
#             backtracking(arr+')', openCount, closeCount+1)
#     backtracking("", 0, 0)
#     return result





def parenthesis(n):
    result = []

    def backtracking(arr, total):
        if len(arr) == n*2:
            if total == 0:
                result.append(arr)
            return
        
        if total < n:
            backtracking(arr+'(', total+1)
        if total > 0:
            backtracking(arr+')', total-1)
    backtracking("", 0)
    return result

print(parenthesis(n))