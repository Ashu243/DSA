ops = ["5","2","C","D","+"]

def baseball_game(ops):
    stack = []
    sum = 0
    for op in ops:
        if op == 'C':
            num = stack.pop()
            sum -= num
        elif op == 'D':
            ans = stack[-1]*2
            stack.append(ans)
            sum += ans
        elif op == '+':
            ans = stack[-1]+stack[-2]
            stack.append(ans)
            sum += ans
        else:
            stack.append(int(op))
            sum += int(op)
    return sum

print(baseball_game(ops))