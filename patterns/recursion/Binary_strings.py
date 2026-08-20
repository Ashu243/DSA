n = 3

def binary_str(n):
    arr = [0]*n
    result = []

    def backtracking(index, istrue, arr):
        if index == n:
            result.append(arr.copy())
            return
        
        backtracking(index+1, True, arr)
        if istrue:
            arr[index] = 1
            backtracking(index+1, False, arr)
            arr[index] = 0
    
    backtracking(0, True, arr)
    return result
print(binary_str(n))
