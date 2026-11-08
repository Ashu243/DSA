s = "abcabc"

def no_of_substrings(s):
    left = 0
    result = 0
    freq_dict = {
        'a' : -1,
        'b' : -1,
        'c' : -1
    }
    formed = 0
    n = len(s)

    for right in range(n):
        freq_dict[s[right]] += 1
        if freq_dict[s[right]] == 0:
            formed += 1
        
        while formed == 3:
            result += n - right
            if freq_dict[s[left]] == 0:
                formed -= 1
            freq_dict[s[left]] -= 1
            left += 1

    
    return result

print(no_of_substrings(s))

