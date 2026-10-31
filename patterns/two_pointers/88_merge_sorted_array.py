nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

def merge_sorted_array(nums1, m, nums2, n):
    p1, p2 = 0, 0
    nums = [0]*(m+n)
    i = 0

    while p1 < m and p2 < n:
        if nums1[p1] <= nums2[p2]:
            nums[i] = nums1[p1]
            p1 += 1
        else:
            nums[i] = nums2[p2]
            p2 += 1
        i += 1
    
    while p1 < m:
        nums[i] = nums1[p1]
        p1 += 1
        i += 1
    while p2 < n:
        nums[i] = nums2[p2]
        p2 += 1
        i += 1
    
    for i in range(len(nums)):
        nums1[i] = nums[i]
    
    return nums1

print(merge_sorted_array(nums1, m, nums2, n))