temperatures = [73,74,75,71,69,72,76,73]


def daily_temp(temperatures):
    stack = []
    n = len(temperatures)
    ans = [0]*n

    for i in range(n-1, -1, -1):
        day = 0
        while stack and stack[-1][0] <= temperatures[i]:
            stack.pop()
        if stack:
            # index of stack[-1] - index of current temperature
            day = stack[-1][1] - i
        ans[i] = day
        stack.append([temperatures[i], i])
    return ans

print(daily_temp(temperatures))
