class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                t1 = stack.pop()
                t2 = stack.pop()
                ans = 0
                
                if token == '+':
                    ans = t1+t2
                elif token == '-':
                    ans = t2-t1
                elif token == '*':
                    ans = t1*t2
                else:
                    ans = int(t2 / t1)
                stack.append(ans)
            else:
                stack.append(int(token))
        
        return stack[0]


