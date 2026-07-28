import math
piles = [3,6,7,11]
h = 8

def koko_eating(piles, h):

    def can_eat(bananas):
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i] / bananas)
            if hours > h:
                return False
        return True


    left = 1
    right = max(piles)
    result = 0

    while left <= right:
        mid = (left+right) // 2

        if can_eat(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

print(koko_eating(piles, h))

            