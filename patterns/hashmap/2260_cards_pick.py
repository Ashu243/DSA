class Solution:
    def minimumCardPickup(self, nums: list[int]) -> int:
        nums_dict = {}
        min_len = float('inf')

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                min_len = min(min_len, i - nums_dict[nums[i]] + 1)
            nums_dict[nums[i]] = i
        
        return min_len if min_len != float('inf') else -1