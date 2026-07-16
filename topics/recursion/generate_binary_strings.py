n = 3

def generate_strings(n):
    arr = ["0"]*n
    result = []

    def solve(index, flag, arr, result):
        if len(arr) == index:
            result.append("".join(arr))
            return
        
        arr[index] = "0"
        solve(index+1, True, arr, result)

        if flag == True:
            arr[index] = "1"
            solve(index+1, False, arr, result)
            arr[index] = "0"
    
    solve(0, True, arr, result)
    return result

print(generate_strings(n))


# n = 3

# def generate_strings(n):
#     arr = ["0"]*n
#     result = []

#     def solve(index, arr, result):
#         if len(arr) == index:
#             result.append("".join(arr))
#             return
        
#         arr[index] = "0"
#         solve(index+1, arr, result)

#         arr[index] = "1"
#         solve(index+1, arr, result)
    
#     solve(0, arr, result)
#     return result

# print(generate_strings(n))