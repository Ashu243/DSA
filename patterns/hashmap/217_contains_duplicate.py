nums = [1,2,3,1]

def contains_duplicate(nums):
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False