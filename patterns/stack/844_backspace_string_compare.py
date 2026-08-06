s = "y#fo##f"
t = "y#f#o##f"


def compare(s, t):
    stack_s = []
    stack_t = []
    for i in range(len(s)):
        if s[i] == '#':
            if stack_s:
                stack_s.pop(-1)
        else:
            stack_s.append(s[i])
    for ch in t:
        if ch == '#':
            if stack_t:
                stack_t.pop(-1)
        else:
            stack_t.append(ch)
    return stack_s == stack_t

print(compare(s, t))