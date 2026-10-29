pattern = "abba"
s = "dog cat dog cat"


def word_pattern(pattern, s):
    splitstr = s.split(' ')
    if len(splitstr) != len(pattern):
        return False

    char_map = {}
    word_map = {}

    for i in range(len(pattern)):
        if pattern[i] in char_map and splitstr[i] != char_map[pattern[i]]:
            return False
        if splitstr[i] in word_map and pattern[i] != word_map[splitstr[i]]:
            return False
        char_map[pattern[i]] = splitstr[i]
        word_map[splitstr[i]] = pattern[i]
    
    return True

print(word_pattern(pattern, s))
