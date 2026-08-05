nums = ["ab", "aa", "aa", "bcd", "ab"]

def remove_consecutive(nums):
    ans = [nums[0]]

    for i in range(1, len(nums)):
        if not ans:
            ans.append(nums[i])
            continue
        elif nums[i] == ans[-1]:
            ans.pop()
        else:
            ans.append(nums[i])
    
    return len(ans)

print(remove_consecutive(nums))