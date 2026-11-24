n = 3

# def binary_str(n):
#     arr = [0]*n
#     result = []

#     def backtracking(index, istrue, arr):
#         if index == n:
#             result.append(arr.copy())
#             return
        
#         backtracking(index+1, True, arr)
#         if istrue:
#             arr[index] = 1
#             backtracking(index+1, False, arr)
#             arr[index] = 0
    
#     backtracking(0, True, arr)
#     return result
# print(binary_str(n))

def binary_str(n):
    result = []
    
    def recursion(path):
        if len(path) == n:
            result.append("".join(map(str, path)))
            return
        
        path.append(0)
        
        recursion(path)
        path.pop()
        path.append(1)
        recursion(path)
        path.pop()
    
    recursion([])
    return result

print(binary_str(n))
