strs = ["eat","tea","tan","ate","nat","bat"]


def group_anagram(strs):

    mydict = {}
    for word in strs:
        wordlist = []

        # converting each ch into ascii code 
        for ch in word:
            wordlist.append(ord(ch))
        
        # sorting the list so all the anagram words become same
        wordlist.sort()

        # joining the word
        sortedword = ''.join(chr(val) for val in wordlist)

        mydict.setdefault(sortedword, []).append(word)


    return list(mydict.values())
print(group_anagram(strs))