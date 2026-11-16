nums = [3,5,2,6]
k = 2

def competitive_subsequence(nums, k):
    stack = []
    removal_budget = len(nums) - k

    for num in nums:
        while stack and stack[-1] > num and removal_budget > 0:
            stack.pop()
            removal_budget -= 1

        stack.append(num)
    
    return stack[:k]

print(competitive_subsequence(nums, k))