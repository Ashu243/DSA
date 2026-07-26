def isPerfectSquare(self, x: int) -> bool:
    left = 0
    right = x

    while left<=right:
        mid = (left+right)//2
        sq = mid*mid
        if sq == x:
            return True
        elif sq > x:
            right = mid - 1
        
        else:
            left = mid + 1
    return False