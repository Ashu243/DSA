s = "ADOBECODEBANC"
t = "ABC"


def minimum_window(s, t):
    freq_dict = {}

    for char in t:
        freq_dict[char] = freq_dict.get(char, 0) - 1
    
    left = 0
    minimum_sub = ''
    required = len(freq_dict)
    formed = 0

    for right in range(len(s)):
        if s[right] in freq_dict:
            freq_dict[s[right]] += 1
            if freq_dict[s[right]] == 0:
                formed += 1
        while formed == required:
            if minimum_sub == '':
                minimum_sub = s[left:right+1]
            elif right - left + 1 < len(minimum_sub):
                minimum_sub = s[left:right+1]

            if s[left] in freq_dict:
                if freq_dict[s[left]] == 0:
                    formed -= 1
                freq_dict[s[left]] -= 1

            left += 1
    
    return minimum_sub

print(minimum_window(s, t))
            
            
