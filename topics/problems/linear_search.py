
nums = [1, 20, 48, 34, 23, 95, 38, 47, 82, 73]

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
        

result = linear_search(nums, 38)

if result == -1:
    print('value not found in the array')
else:
    print(f'value found at {result}')
