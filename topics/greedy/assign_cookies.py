greed = [2, 6, 8, 1, 4]
s = [4, 2, 7, 1, 2, 3]

def assign_cookies(greed, s):
    greed.sort()
    s.sort()
    left = 0
    right = 0
    cookie_assigned = 0

    while left< len(greed) and right < len(s):
        if greed[left] <= s[right]:
            cookie_assigned += 1
            left += 1
            right += 1

        else:
            right += 1

    return cookie_assigned

print(assign_cookies(greed, s))
