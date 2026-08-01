strs = ["eat","tea","tan","ate","nat","bat"]

# def group_anagram(strs):
#     mydict = {}

#     for word in strs:
#         wordlist = []
#         for ch in word:
#             wordlist.append(ord(ch))
#         wordlist.sort()

#         sortedword = ''.join(chr(val) for val in wordlist)
#         mydict.setdefault(sortedword, []).append(word)

#     return list(mydict.values())


def group_anagram(strs):
    mydict = {}

    for word in strs:
        sortedword = ''.join(sorted(word))
        mydict.setdefault(sortedword, []).append(word)
    
    return list(mydict.values())

print(group_anagram(strs))