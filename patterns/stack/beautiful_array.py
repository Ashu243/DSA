nums = [-1, 0, 0, 0, 0]


def beautiful_arr(nums):
    ans = [nums[0]]

    for i in range(1, len(nums)):
        if not ans:
            ans.append(nums[i])
            continue
        elif nums[i] < 0 and ans[-1] >= 0:
            ans.pop(-1)
        elif nums[i] >= 0 and ans[-1] < 0:
            ans.pop(-1)
        else:
            ans.append(nums[i])
    return ans

print(beautiful_arr(nums))