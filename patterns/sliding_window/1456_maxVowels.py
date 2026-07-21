s = "abciiidef"
k = 3

def maxVowels(s, k):
    Vset = {'a', 'e', 'i', 'o', 'u'}
    left = 0
    vowelcount = 0
    maxcount = 0
    for right in range(len(s)):
        if s[right] in Vset:
            vowelcount += 1
        
        if right - left + 1 == k:
            maxcount = max(maxcount, vowelcount)
            if s[left] in Vset:
                vowelcount -= 1
            left += 1
    return maxcount

print(maxVowels(s, k))
