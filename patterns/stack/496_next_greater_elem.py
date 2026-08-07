nums1 = [4,1,2]
nums2 = [1,3,4,2]

def nextGreaterElem(nums1, nums2):
    stack = []
    numsdict = {}

    # loop through each elem from the right and stores the next greater element in map/dictionary
    for i in range(len(nums2)-1, -1, -1):
        while stack and nums2[i] > stack[-1]:
            stack.pop()
        if stack:
            numsdict[nums2[i]] = stack[-1]
        else:
            numsdict[nums2[i]] = -1
        stack.append(nums2[i])
    
    # get the next greater elem from the dictionary and update it in place. can be also done using another array to avoid in place changes
    for i in range(len(nums1)):
        nums1[i] = numsdict[nums1[i]]

    return nums1

print(nextGreaterElem(nums1, nums2))
