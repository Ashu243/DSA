nums = [3,1,-2,-5,2,-4]

def arrange_elem(nums):
    n = len(nums)
    result = [0] * n

    j = 0
    k = 1
    for i in range(n):
        if nums[i] > 0:
            result[j] = nums[i]
            j += 2
        else:
            result[k] = nums[i]
            k += 2


    return result


print(arrange_elem(nums))

