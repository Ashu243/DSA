nums = [0,0,0,0,0]
goal = 0


def numSubarraysWithSum(nums, goal):
    n = len(nums)
    prefix_sum = 0
    
    numsdict = {}
    result = 0

    for right in range(n):
        prefix_sum += nums[right]
        if prefix_sum == goal:
            result += 1

        ans = prefix_sum - goal
        if ans in numsdict:
            result += numsdict[ans]

        numsdict[prefix_sum] = numsdict.get(prefix_sum, 0) + 1
    
    return result
print(numSubarraysWithSum(nums, goal))