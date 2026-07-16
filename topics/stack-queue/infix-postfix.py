
def precedence(ch):
    if ch == '+' or ch == '-':
        return 1
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '^':
        return 3
    return 0

def InfixtoPostfix(s):
    stack = []
    ans = []

    for char in s:
        if ("a" <= char <= "z") or ("A" <=char <= "Z") or ("0" <= char <= "9"):
            ans.append(char)
        elif char == '(':
            stack.append(char)
        
        elif char == ')':
            while stack and stack[-1]!= '(':
                ans.append(stack.pop())
            stack.pop()
        else:
            while stack and (
                precedence(char) < precedence(stack[-1]) or
                (precedence(char) == precedence(stack[-1]) and char != '^')
            ):
                ans.append(stack.pop())
            stack.append(char)
    
    while stack:
        ans.append(stack.pop())
    return "".join(ans)

print(InfixtoPostfix("a+b*(c^d-e)"))



# postfix to infix

def postToInfix(self, postfix):
    stack = []
    for ch in postfix:
        if ch.isalnum():
            stack.append(ch)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            new_elem = f"({operand1}{ch}{operand2})"
            
            stack.append(new_elem)
    
    return stack[0]