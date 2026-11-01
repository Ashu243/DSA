nums = [10,20,30,40,50,60,70,80,90]
target = 1

def three_sum_closet(nums, target):
    nums.sort()
    ans = float('inf')
    result = 0
    n = len(nums)

    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = n - 1

        while j<k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                return sum
            if ans > abs(target-sum):
                ans = abs(target-sum)
                result = sum
                
            
            if sum < target:
                j += 1
            elif sum > target:
                k -= 1
    return result

print("ans", three_sum_closet(nums, target))