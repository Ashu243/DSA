s = "badc"
t = "baba"

def isomorphic_string(s, t):
    char_map = {}
    char_map2 = {}

    for i in range(len(s)):
        if s[i] in char_map and t[i] != char_map[s[i]]:
            return False
        if t[i] in char_map2 and s[i] != char_map2[t[i]]:
            return False
        char_map[s[i]] = t[i]
        char_map2[t[i]] = s[i]

    return True

print(isomorphic_string(s, t))