s = "100[leetcode]"

def decode_string(s):
    numStack = []
    stack = []
    i = 0

    while i < len(s):
        if s[i] in 'abcdefghijklmnopqrstuvwxyz[':
            stack.append(s[i])
        elif s[i] == ']':
            j = len(stack)-1
            string = []
            while stack[j] != '[':
                string.append(stack.pop())
                j -= 1
            # removes the '['
            stack.pop()

            string = string*int(numStack.pop())

            while string:
                stack.append(string.pop())
        else:
            num = ''
            while s[i] != '[':
                num += s[i]
                i+= 1
            numStack.append(num)
            continue
        i+= 1
    
    return ''.join(ch for ch in stack)

print(decode_string(s))