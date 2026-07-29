
time = [1,2,3]
totalTrips = 5

def min_time(time, totalTrips):

    def can_trip(hours):
        count = 0
        for t in time:
            count += hours // t
            if count >= totalTrips:
                return True
        return False

    left = 1
    right = min(time) * totalTrips

    while left <= right:
        mid = (left+right) // 2
        if can_trip(mid):
            right = mid - 1
        else:
            left = mid+1
    return left
    

print(min_time(time, totalTrips))