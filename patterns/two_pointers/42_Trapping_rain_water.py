height = [0,1,0,2,1,0,1,3,2,1,2,1]


# def trapping_rain_water(height):
#     n = len(height)
    
#     rightmax = 0
#     right = 0

#     for i in range(n):
#         if rightmax < height[i]:
#             rightmax = height[i]
#             right = i

#     leftmax = height[0]
#     sum = 0
#     for i in range(1, right):
#         minHB = min(leftmax, rightmax)
#         water = minHB - height[i]
#         if water<0:
#             sum = sum + 0
#         else:
#             sum = sum + water
#         if leftmax < height[i]:
#             leftmax = height[i]
    
#     rightmax = height[-1]
#     for i in range(n-2, right, -1):

#         minHB = min(leftmax, rightmax)
#         water = minHB - height[i]
#         if water<0:
#             sum = sum + 0
#         else:
#             sum = sum + water
#         if rightmax < height[i]:
#             rightmax = height[i]
      
#     return sum

# print(trapping_rain_water(height))


# TWO POINTER APPROACH

def trapping_rain_water(height):
    left = 0
    right = len(height)-1

    leftmax = 0
    rightmax = 0

    total_water = 0
    while left < right:
        leftmax = max(leftmax, height[left])

        rightmax = max(rightmax, height[right])

        if leftmax < rightmax:
            total_water += (leftmax - height[left])
            left += 1
        
        else:
            total_water += rightmax - height[right]
            right -= 1
        
    return total_water

print(trapping_rain_water(height))
