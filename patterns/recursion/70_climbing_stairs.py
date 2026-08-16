n = 4

memo = {}
def climbing_stairs(n):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2 or n == 0:
        return n
    
    memo[n] = climbing_stairs(n-1) + climbing_stairs(n-2)
    return memo[n]

print(climbing_stairs(n))