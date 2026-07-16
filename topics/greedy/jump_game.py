nums = [1,0,2,3]

def jump_game(nums):
    n = len(nums)

    reachable_index = 0

    for i in range(n):
        if i > reachable_index:
            return False
        reachable_index = max(reachable_index, i + nums[i])
    return True


print(jump_game(nums))