x = 8

def mySqrt(x):
    left = 0
    right = x
    result = -1

    while left<=right:
        mid = (left+right)//2
        sq = mid*mid
        if sq == x:
            return mid
        elif sq > x:
            right = mid - 1
        
        else:
            result = mid
            left = mid + 1
    return result

print(mySqrt(x))