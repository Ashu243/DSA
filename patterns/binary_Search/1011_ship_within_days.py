weights = [3,2,2,4,1,4]
days = 3

def ship_in_days(weights, days):

    def min_weight(wt):
        count = 0
        sum = 0
        for weight in weights:
            sum += weight
            if sum > wt:
                count += 1
                sum = weight
        if sum <= wt:
            count += 1
        return count <= days


    left = max(weights)
    right = sum(weights)

    while left <= right:
        mid = (left+right) // 2
        
        if min_weight(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

print(ship_in_days(weights, days))