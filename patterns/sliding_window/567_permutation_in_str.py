s1 = "ab"
s2 = "eidbaooo"


def permutationStr(s1, s2):
    n = len(s1)
    freqdict = {}
    for i in range(n):
        freqdict[s1[i]] = freqdict.get(s1[i], 0) + 1

    left = 0
    freqdict2 = {}
    for right in range(len(s2)):
        freqdict2[s2[right]] = freqdict2.get(s2[right], 0)+1

        if right - left + 1 == n:
            if freqdict == freqdict2:
                return True
            freqdict2[s2[left]] = freqdict2[s2[left]]-1
            if freqdict2[s2[left]] == 0:
                freqdict2.pop(s2[left])
            left += 1
    return False

print(permutationStr(s1, s2))


