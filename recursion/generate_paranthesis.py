n = 2

# def generate_parenthesis(n):
#     result = []
#     arr = [""]*(2*n)
#     def solve(index, arr, result, total):
#         if index == len(arr):
#             if total == 0:
#                 result.append("".join(arr))
#             return
        
#         if total> len(arr)//2:
#             return
#         elif total < 0:
#             return
#         arr[index] = "("
#         total = total + 1
#         solve(index+1, arr, result, total)
#         arr[index] = ")"
#         total = total - 1
#         solve(index+1,arr, result, total)

#     solve(0, arr, result, 0)
#     return result
        

# def generate_parenthesis(n):
#     result = []
#     arr = [""]*(2*n)

#     def solve(index, total, arr, result):
#         if index == len(arr):
#             if total == 0:
#                 result.append(''.join(arr))
#             return
        
#         if total < len(arr)//2:
#             arr[index] = '('
#             sum = total + 1
#             solve(index+1, sum, arr, result)
        
#         if total>0:
#             arr[index] = ')'
#             sum = total - 1
#             solve(index+1, sum, arr, result)

#     solve(0, 0, arr, result)
#     return result


# print(generate_parenthesis(n))


# ()()
def generate_parenthesis(n):
    result = []

    def backtrack(current, open_count, closed_count):
        if len(current) == 2*n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count+1, closed_count)
        
        if closed_count < open_count:
            backtrack(current+')', open_count, closed_count+1)

    backtrack("", 0, 0)
    return result

print(generate_parenthesis(n))