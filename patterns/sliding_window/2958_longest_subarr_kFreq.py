nums = [2,2,3]
k = 1

# my invented solution
# def longest_subarr(nums, k):
#     numsdict = {}
#     maxFreq = [0, 0]
#     left = 0
#     maxlen = 0

#     for right in range(len(nums)):
#         numsdict[nums[right]] = numsdict.get(nums[right], 0) + 1
#         if numsdict[nums[right]] > maxFreq[0]:
#             maxFreq[0] = numsdict[nums[right]]
#             maxFreq[1] = nums[right]

#         while maxFreq[0] > k:
#             numsdict[nums[left]] -= 1
#             if maxFreq[1] == nums[left]:
#                 maxFreq[0] -= 1
#             left += 1

#         maxlen = max(maxlen, right-left+1)
    
#     return maxlen


# print(longest_subarr(nums, k))


# standard solution

def longest_subarr(nums, k):
    left = 0
    freq = {}
    maxlen = 0

    for right in range(len(nums)):
        freq[nums[right]] = freq.get(nums[right], 0) + 1

        while freq[nums[right]] > k:
            freq[nums[left]] -= 1
            left += 1

        maxlen = max(maxlen, right-left+1)

    return maxlen

print(longest_subarr(nums, k))