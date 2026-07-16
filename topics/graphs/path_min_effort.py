import heapq
heights = [[1,2,3],[3,8,4],[5,3,5]]

def path_min_effort(heights):
    row = len(heights)
    col = len(heights[0])

    distance = [[float('inf') for _ in range(col)] for _ in range(row)]
    distance[0][0] = 0

    priority_queue = [(0, 0, 0)]
    directions = [(0,1), (-1, 0), (1, 0), (0, -1)]

    while priority_queue:
        effort, u, v = heapq.heappop(priority_queue)


        if u == row-1 and v == col-1:
            return effort

        for dr, dc in directions:
            nr = dr+u
            nc = dc + v
            if nr>=0 and nr<row and nc>=0 and nc<col:
                difference = abs(heights[nr][nc] - heights[u][v])
                max_effort = max(effort, difference)
                if distance[nr][nc] > max_effort:
                    distance[nr][nc] = max_effort
                    heapq.heappush(priority_queue, (max_effort, nr, nc))

print(path_min_effort(heights))