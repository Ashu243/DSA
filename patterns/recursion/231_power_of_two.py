n = 16

def ispower2(n, power):
    ans = 2**power
    if ans > n:
        return False
    if ans == n:
        return True
    return ispower2(n, power+1)

print(ispower2(n, 0))