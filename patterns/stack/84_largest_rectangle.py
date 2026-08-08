heights = [2,1,5,6,2,3]


def largest_rectangle(heights):
    nsl = []
    stack = []
    n = len(heights)
    nsr = [0]*n

    for i in range(n):
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        if stack:
            nsl.append(stack[-1][1])
        else:
            nsl.append(-1)
        stack.append([heights[i], i])
    
    stack.clear()

    for i in range(n-1, -1, -1):
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        if stack:
            nsr[i] = stack[-1][1]
        else:
            nsr[i] = n
        stack.append([heights[i], i])
    
    max_area = 0
    for i in range(n):
        width = nsr[i] - nsl[i] - 1
        max_area = max(heights[i]*width, max_area)
    
    return max_area

print(largest_rectangle(heights))
