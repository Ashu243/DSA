asteroids = [3,5,-6,2,-1,4]

def asteriod_collison(asteroids):
    stack = []

    for ast in asteroids:
        if ast > 0:
            stack.append(ast)
        else:
            while stack and stack[-1]>0 and stack[-1] < abs(ast):
                stack.pop()
            if stack and stack[-1] == abs(ast):
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(ast)
    return stack

print(asteriod_collison(asteroids))