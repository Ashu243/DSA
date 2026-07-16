string = '({[]})'

# def valid_parenthesis(string):
#     stack = []
#     for i in range(len(string)):
#         if string[i] == '(' or string[i] == '{' or string[i] == '[':
#             stack.append(string[i])
#         if string[i] == ')' or string[i] == '}' or string[i] == ']':
#             poped_bracket = stack.pop()
#             result = poped_bracket+string[i]
#             if result != '()' and result != '[]' and result != "{}":
#                 return False
#     if len(stack) == 0:
#         return True
#     return False

def valid_parenthesis(string):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    print(pairs[')'])

    for ch in string:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0

print(valid_parenthesis(string))