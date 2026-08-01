nums = [1,2,3,1]


def contains_duplicate(nums):
    numsSet = set()
    for i in range(len(nums)):
        if nums[i] in numsSet:
            return True
        numsSet.add(nums[i])
    return False