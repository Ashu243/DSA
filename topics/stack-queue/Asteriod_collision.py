nums = [5, 12,10 , -7, 9, -12]

def asteriod_collision(nums):
    stack = []
    n = len(nums)

    for i in range(n):
        if nums[i]>0:
            stack.append(nums[i])
        else:
            while stack and stack[-1]>0 and stack[-1]<abs(nums[i]):
                stack.pop()
            if stack and stack[-1] == abs(nums[i]):
                stack.pop()
            elif not stack or stack[-1]<0:
                stack.append(nums[i])
    return stack

print(asteriod_collision(nums))
