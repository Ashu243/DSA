nums = [1,7,3,6,5,6]

# optimal
def pivotindex(nums):
    n = len(nums)
    total = sum(nums)
    left = 0

    for i in range(n):
        right = total - left - nums[i]

        if right == left:
            return i
        left += nums[i]
    return -1

# brute force
# def pivotindex(nums):
#         n = len(nums)
#         presum = [nums[0]]*n
#         suffixsum = [nums[-1]]*n

#         for i in range(n-2, -1, -1):
#             suffixsum[i] = nums[i] + suffixsum[i+1]
            
#         for i in range(1, n):
#             presum[i] = nums[i] + presum[i-1]
        
#         for i in range(n):
#             if suffixsum[i] == presum[i]:
#                 return i
#         return -1
print(pivotindex(nums))