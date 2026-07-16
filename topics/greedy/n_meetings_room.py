start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]

def n_meetings_room(start, end):
    meetings = []

    for i in range(len(end)):
        meetings.append([end[i], start[i]])
    meetings.sort()

    count = 1
    last_end = meetings[0][0]
    for i in range(1, len(meetings)):
        if meetings[i][1] > last_end:
            count += 1
            last_end = meetings[i][0]
    
    return count

print(n_meetings_room(start, end))
