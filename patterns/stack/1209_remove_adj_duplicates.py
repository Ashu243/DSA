# optimal approach

def optimalremoveDuplicates(self, s: str, k: int) -> str:
    stack = []

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])
        
        if stack[-1][1] == k:
            stack.pop()
    
    return ''.join(char * count for char, count in stack)

# not optimal approach
def removeDuplicates(self, s: str, k: int) -> str:
    stack = []

    for i in range(len(s)):
        if len(stack) >= k-1:
            count = 1
            poped = []
            while stack and stack[-1] == s[i] and count < k:
                poped.append(stack.pop())
                count += 1
            if count == k:
                continue
            else:
                while poped:
                    stack.append(poped.pop())

        stack.append(s[i])
    
    return ''.join(x for x in stack)