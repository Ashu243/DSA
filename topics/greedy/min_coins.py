coins = [1,2,5,10]
n = 121


def min_coins(coins, n):

    i = len(coins)-1
    ans = 0
    while n != 0:
        while n<coins[i]:
            i -= 1
        n = n - coins[i]
        ans += 1

    return ans

print(min_coins(coins, n))