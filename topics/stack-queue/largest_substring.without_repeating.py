s = 'pwwkew'

def substring_without_repeat(s):
    n = len(s)
    my_dict = {}
    left, right = 0, 0

    maximum = 0

    while right<n:
        if s[right] in my_dict:
            left = max(left, my_dict[s[right]]+1)


        maximum = max(maximum, right-left+1)
        my_dict[s[right]] = right
        right += 1

    return maximum

print(substring_without_repeat(s))