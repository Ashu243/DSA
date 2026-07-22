s = "abba"


def lengthOfLongestSubstring(s):
    left = 0
    mydict = {}
    maxlen = 0

    for right in range(len(s)):
        if s[right] in mydict:
            left = max(left, mydict[s[right]]+1) # in this s = "abba", when right is on last a then the left can go to 0+1 that's why we use max(left, ...)
        print(mydict)

        mydict[s[right]] = right

        maxlen = max(maxlen, right-left+1)
    
    return maxlen

print(lengthOfLongestSubstring(s))