height = [1,8,6,2,5,4,8,3,7]


def container_water(height):
    left = 0 
    right = len(height)-1
    max_water = 0

    while left < right:
        min_height = min(height[left], height[right])
        area = min_height * (right-left)
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

print(container_water(height))