s = "AABABBA"
k = 1


def characterReplacement(s, k):
    left = 0
    maxfreq = 0
    freqdict = {}
    maxlen = 0

    for right in range(len(s)):
        freqdict[s[right]] = freqdict.get(s[right], 0) + 1
        if freqdict[s[right]] > maxfreq:
            maxfreq = freqdict[s[right]]
        
        window = right - left + 1 
        if window - maxfreq <= k:
            maxlen = max(maxlen, window)
        while window - maxfreq > k:
            freqdict[s[left]] = freqdict[s[left]]-1
            left += 1
            window -= 1
    return maxlen

print(characterReplacement(s, k))