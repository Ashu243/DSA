heights = [10,6,8,5,11,9]

def canSeePersonsCount(heights):
    stack = []
    n = len(heights)
    ans = [0]*n

    for i in range(n-1, -1, -1):
        person = 0
        # increase the count of the person shorter than current and pop from stack
        while stack and stack[-1] < heights[i]:
            person += 1
            stack.pop()
        # if there is a person in stack - means he/she is taller than current person which is not removed from the stack but can see him
        if stack:
            ans[i] = person+1
        else:
            ans[i] = person
        stack.append(heights[i])
    
    return ans

print(canSeePersonsCount(heights))
        