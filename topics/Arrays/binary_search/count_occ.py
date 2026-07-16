nums = [1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 8, 9, 9]
target = 9

def count_occ(nums, target):
    def lower_bound(nums, target):
        left = 0
        right = len(nums)-1
        lb = -1
        while left<=right:
            mid = (left+right) // 2
            if nums[mid]>=target:
                lb = mid
                right = mid-1
            else:
                left = mid+1
        return lb
    result1 = lower_bound(nums, target)
    if result1 == -1 or nums[result1] != target:
        return 0 

    def upper_bound(nums, target):
        left = 0
        right = len(nums)-1
        ub = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<=target:
                ub = mid
                left = mid+1
            else:
                right = mid-1
        return ub
    
    result2 = upper_bound(nums, target)
    
    return (result2 -result1)+1
print(count_occ(nums, target))
