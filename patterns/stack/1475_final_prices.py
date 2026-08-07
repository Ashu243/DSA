prices = [8,4,6,2,3]

def finalPrices(prices):
    n = len(prices)
    stack = []
    result = [0]*n
    for i in range(n-1, -1, -1):
        while stack and prices[i] < stack[-1]:
            stack.pop()
        if stack:
            result[i] = prices[i]-stack[-1]
        else:
            result[i] = prices[i]
        stack.append(prices[i])
    return result

print(finalPrices(prices))