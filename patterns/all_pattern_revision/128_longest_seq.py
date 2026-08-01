nums = [100,4,200,1,3,2]

def longest_seq(nums):
    num_set = set(nums)
    max_count = 0

    for num in num_set:
        if num - 1 not in num_set:
            count = 1
            x = num

            while x + 1 in num_set:
                x += 1
                count += 1
            max_count = max(count, max_count)
    
    return max_count
print(longest_seq(nums))




