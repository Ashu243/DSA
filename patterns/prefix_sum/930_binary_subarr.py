nums = [0,0,0,0,0]
goal = 0

def binary_subarr(nums, goal):
    prefix_sum = 0
    numsdict = {0: 1}
    result = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        ans = prefix_sum - goal
        if ans in numsdict:
            result += numsdict[ans]

        numsdict[prefix_sum] = numsdict.get(prefix_sum, 0) + 1
    return result

print(binary_subarr(nums, goal))
