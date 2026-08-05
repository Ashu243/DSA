s = "())"

def make_valid(s):
    pairs = {')':'(', ']':'[', '}': '{'}
    stack = []
    count = 0

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                stack.append(ch)
            else:
                stack.pop(-1)
    return len(stack)

print(make_valid(s))