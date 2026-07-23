s = "cbaebabacd"
p = "abc"


def findAnagrams(s, p):
    n = len(p)
    freqdict = {}
    for i in range(n):
        freqdict[p[i]] = freqdict.get(p[i], 0) + 1
    
    left = 0
    Sfreqdict = {}
    result = []

    for right in range(len(s)):
        Sfreqdict[s[right]] = Sfreqdict.get(s[right], 0) + 1

        if right - left + 1 == n:
            if freqdict == Sfreqdict:
                result.append(left)
            Sfreqdict[s[left]] = Sfreqdict[s[left]]-1
            if Sfreqdict[s[left]] == 0:
                Sfreqdict.pop(s[left])
            left += 1
    return result


print(findAnagrams(s, p))
