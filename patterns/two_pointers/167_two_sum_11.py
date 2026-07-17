numbers = [2,7,11,15]
target = 9

def two_sum(numbers, target):
    left = 0
    right = len(numbers)-1

    while left <= right:
        sum = numbers[left]+ numbers[right]
        if sum > target:
            right -= 1
        elif sum == target:
            return left+1, right+1
        else:
            left += 1

print(two_sum(numbers, target))
    
