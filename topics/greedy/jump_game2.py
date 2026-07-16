nums = [1,2,1,1,1]


def jump_game2(nums):
    jumps = 0
    farthest = 0
    current_end = 0

    for i in range(len(nums)-1):
        farthest = max(farthest, i+nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
    
print(jump_game2(nums))