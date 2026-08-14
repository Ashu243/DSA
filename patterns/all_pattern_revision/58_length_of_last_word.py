s = "   fly me   to   the moon  "


def last_word(s):
    string = s.rstrip()
    max_len = 0
    for i in range(len(string)-1, -1, -1):
        if s[i] == ' ':
            return max_len
        max_len+= 1
    return max_len

print(last_word(s))
