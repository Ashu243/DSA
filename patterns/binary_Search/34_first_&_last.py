class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        def first_p():
            left = 0
            right = len(nums)-1

            while left < right:
                mid = (left+right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return left if nums[left] == target else -1
        
        def last_p():
            left = 0
            right = len(nums)-1

            while left < right:
                mid = (left+right+1) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return left if nums[left] == target else -1
        
        ans1 = first_p()
        ans2 = last_p()
        return [ans1, ans2]
