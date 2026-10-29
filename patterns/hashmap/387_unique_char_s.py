s = "loveleetcode"


def unique_string(s):

    nums_arr = [-1]*26

    for i in range(len(s)):
        num = 97 - ord(s[i])
        nums_arr[num] += 1
    
    for i in range(len(s)):
        if nums_arr[97-ord(s[i])] == 0:
            return i
    return -1

print(unique_string(s))
