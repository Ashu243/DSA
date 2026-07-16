s = "anagram"
t = "nagaran"

def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    else:
        mydict = {}
        for i in range(len(s)):
            mydict[s[i]] = mydict.get(s[i], 0) + 1
            mydict[t[i]] = mydict.get(t[i], 0) - 1
    
    for value in mydict.values():
        if value != 0:
            return False
    
    return True

print(valid_anagram(s, t))

