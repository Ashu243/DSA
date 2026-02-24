nums = [100,4,200,1,3,2]

def largest_consc(nums):
    n = len(nums)
    count = 0
    max_count = 0
    num = 0
    for i in range(n):
        num = nums[i]
        count = 1
        while num+1 in nums:
            count += 1
            num += 1
        if count> max_count:
            max_count = count
        count = 0
    
    return max_count


print(largest_consc(nums))