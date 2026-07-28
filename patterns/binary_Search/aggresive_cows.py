nums = [1, 2, 4, 8, 9]
k = 3

def aggresive_cows(nums, k):

    def can_place(distance):
        count = 1
        lastplaced = nums[0]
        for i in range(len(nums)):
            if nums[i] - lastplaced >= distance:
                lastplaced = nums[i]
                count += 1
                if count == k:
                    return True
        return False


    left = nums[0]
    right = nums[-1] - left
    ans = 0

    while left <= right:
        mid = (left+right) // 2
        if can_place(mid):
            left = mid+1
            ans = mid
        else:
            right = mid -1

    return ans


print(aggresive_cows(nums, k))
