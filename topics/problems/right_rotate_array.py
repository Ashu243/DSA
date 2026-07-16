
nums = [2, 3, 3, 6, 7, 2, 1, 59, 28, 25]
times = 3

# print(nums[-5:])

# def rotate_array(nums, times):
#     k = times % len(nums) 
#     while k>0:
#         last_elem = nums[len(nums)-1]

#         j = len(nums)-1
#         for i in range(len(nums)-2, -1, -1):
#             nums[j] = nums[i]
#             j -=1

#         nums[0] = last_elem
#         k -= 1

# rotate_array(nums, times)
# print(nums)

n = len(nums)
k = 3

# nums[:] = nums[n-k:] + nums[:n-k]
# print(nums)




def right_rotate(nums, k):

    def reverse(left, right):
        while left< right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, len(nums)-1)
    reverse(0, k-1)
    reverse(k, len(nums)-1)


# right_rotate(nums, 3)
# print(nums)

print(3%10)