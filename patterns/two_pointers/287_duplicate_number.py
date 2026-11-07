nums = [2,5,9,6,9,3,8,9,7,1]


def duplicate_number(nums):
    slow = 0
    fast = 0
    n = len(nums)

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break
    
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

print(duplicate_number(nums))