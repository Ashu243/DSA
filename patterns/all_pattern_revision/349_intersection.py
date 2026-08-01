nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersection(nums1, nums2):
    seen = set(nums1)
    result = set()

    for i in range(len(nums2)):
        if nums2[i] in seen:
            result.add(nums2[i])
            
    return list(result)