nums = [19, 4, 2, 11, 6, 5, 3, 10]


# def brute_next_greater_elem(nums):
#     result = []

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]<nums[j]:
#                 result.append(nums[j])
#                 break
#         else:
#             result.append(-1)

#     return result

# print(brute_next_greater_elem(nums))


def optimal_next_greater_elem(nums):
    n = len(nums)
    stack = []
    ans = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1]<=nums[i]:
            stack.pop()
        if stack and stack[-1] > nums[i]:
            ans.append(stack[-1])
        else:
            ans.append(-1)

        stack.append(nums[i])
    
    return ans[::-1]

print(optimal_next_greater_elem(nums))

def next_greater_elem2(nums):
    n = len(nums)
    stack = []
    ans = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1]<=nums[i]:
            stack.pop()
        stack.append(nums[i])

    for i in range(n-1, -1, -1):
        while stack and stack[-1]<=nums[i]:
            stack.pop()
        if stack and stack[-1] > nums[i]:
            ans.append(stack[-1])
        else:
            ans.append(-1)

        stack.append(nums[i])
    
    return ans[::-1]

