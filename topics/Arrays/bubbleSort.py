arr = [5, 6, 1, 8, 3, 7]

# for i in range(len(arr), -1, -1):
#     for j in range(len(arr) - 1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(len(arr) -2, -1, -1):
    is_swap = False
    for j in range(0, i+1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            is_swap= True
    
    if(is_swap == False):
        break

print(arr)

