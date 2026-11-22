class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        def recursion(index, subset):
            if index == len(nums):
                if subset in result:
                    return
                result.append(subset.copy())
                return
            subset.append(nums[index])
            recursion(index+1, subset)
            subset.pop()
            recursion(index+1, subset)
        
        recursion(0, [])
        return result