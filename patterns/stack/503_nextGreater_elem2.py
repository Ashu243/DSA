nums = [1,2,3,4,3]

def nextGreaterElem2(nums):
    ans = []
    stack = []
    n = len(nums)

    for i in range(n-1, -1, -1):
        while stack and stack[-1] < nums[i]:
            stack.pop()
        stack.append(nums[i])

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(nums[i])
    return ans[::-1]

print(nextGreaterElem2(nums))