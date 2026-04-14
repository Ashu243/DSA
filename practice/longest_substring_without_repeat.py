s = "abcabcbb"


def longest_substring(s):
    n = len(s)
    my_dict = {}
    maximum = 0
    i, j = 0, 0

    while j<n:
        if s[j] in my_dict:
            i = max(i, my_dict[s[j]]+1)


        maximum = max(maximum, j-i+1)
        my_dict[s[j]] = j
        j += 1

    return maximum

print(longest_substring(s))