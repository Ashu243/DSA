haystack = "mississippi"
needle = "issip"



def first_occ(haystack, needle):
    if needle in haystack:
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                j = 0
                while j < len(needle) and haystack[i+j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i
            
    return -1
