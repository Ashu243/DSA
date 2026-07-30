nums = [1000000000,1000000000]
m = 1
k = 1

def bouquets(nums, m, k):

    def make_bouq(day):
        total_bouquets = 0
        count = 0
        for bday in nums:
            if bday <= day:
                count += 1
                if count == k:
                    total_bouquets += 1
                    count = 0
            else:
                count = 0
        return m<=total_bouquets


    left = min(nums)
    right = max(nums)
    ans = 0

    while left<=right:
        mid = (left+right) // 2

        if make_bouq(mid):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    
    return -1 if ans == 0 else ans

print(bouquets(nums, m, k))