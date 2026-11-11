intervals = [[3, 4], [2, 3], [1, 2]]

def right_intervals(intervals):
    intervals_copy = sorted(
        (interval[0], i)
        for i, interval in enumerate(intervals)
    )

    def find_interval(interval):
        end = interval[1]
        left = 0
        right = len(intervals)-1
        while left <= right:
            mid = (left+right) // 2
            if intervals_copy[mid][0] < end:
                left = mid + 1
            else:
                right = mid - 1
        if left < len(intervals_copy):
            result.append(intervals_copy[left][1])
        else:
            result.append(-1)

    result = []

    for interval in intervals:
        find_interval(interval)
    
    return result

print(right_intervals(intervals))