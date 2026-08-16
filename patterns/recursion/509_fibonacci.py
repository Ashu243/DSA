n = 4
memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n == 1 or n == 0:
        return n

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(7))