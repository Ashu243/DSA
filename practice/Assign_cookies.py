g = [2, 6, 8, 1, 4]
s = [4, 2, 7, 1, 2, 3]

def assign_cookies(g, s):
    g.sort()
    s.sort()
    count = 0
    left, right = 0, 0
    while right < len(s):
        if g[left] <= s[right]:
            count += 1
            left += 1
        right += 1


    return count

print(assign_cookies(g, s))
