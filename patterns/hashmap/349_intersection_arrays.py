nums1 = [1,2,2,1]
nums2 = [2,2]

def intersection(nums1, nums2):
    seen = set(nums1)
    result = set()
    
    for i in range(len(nums2)):
        if nums2[i] in seen:
            result.add(nums2[i])
    
    return list(result)
print(intersection(nums1, nums2))