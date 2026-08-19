haystack = "mississippi"
needle = "issip"



def first_occ(haystack, needle):
    if needle in haystack:
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                return i
    
    return -1
