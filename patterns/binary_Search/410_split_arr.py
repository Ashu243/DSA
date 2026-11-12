class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        total_sum = right

        def split_arr(min_sum):
            curr_sum = 0
            splits = 0
            for num in nums:
                curr_sum += num
                if curr_sum > min_sum:
                    splits += 1
                    curr_sum = num
            if curr_sum <= min_sum:
                splits += 1
            if splits <= k:
                return True
            else:
                return False


        while left < right:
            mid = (left+right) // 2
            if split_arr(mid):
                right = mid
            else:
                left = mid + 1
        
        return left