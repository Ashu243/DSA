s = "()[]{}"

def valid_paren(s):
    pairs = {')':'(', ']':'[', '}': '{'}
    stack = []

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop(-1)
    return len(stack)==0

print(valid_paren(s))
        