heights = [2,4]


def largest_rectangle_optimised(heights):
    stack = []
    n = len(heights)
    max_area = 0

    for i in range(n):
        
        while stack and heights[i] < heights[stack[-1]]:
            height = stack.pop()
            if stack:
                nsl = stack[-1]
            else:
                nsl = -1
            ans = heights[height] * (i - nsl -1)
            max_area = max(max_area, ans)
        stack.append(i)
    
    while stack:
        height = stack.pop()
        nsr = n
        if stack:
            nsl = stack[-1]
        else:
            nsl = -1
        ans = heights[height] * (nsr - nsl - 1)
        max_area = max(max_area, ans)
    return max_area

print(largest_rectangle_optimised(heights))

# def largest_rectangle(heights):
#     nsl = []
#     stack = []
#     n = len(heights)
#     nsr = [0]*n

#     for i in range(n):
#         while stack and stack[-1][0] >= heights[i]:
#             stack.pop()
#         if stack:
#             nsl.append(stack[-1][1])
#         else:
#             nsl.append(-1)
#         stack.append([heights[i], i])
    
#     stack.clear()

#     for i in range(n-1, -1, -1):
#         while stack and stack[-1][0] >= heights[i]:
#             stack.pop()
#         if stack:
#             nsr[i] = stack[-1][1]
#         else:
#             nsr[i] = n
#         stack.append([heights[i], i])
    
#     max_area = 0
#     for i in range(n):
#         width = nsr[i] - nsl[i] - 1
#         max_area = max(heights[i]*width, max_area)
    
#     return max_area

# print(largest_rectangle(heights))
