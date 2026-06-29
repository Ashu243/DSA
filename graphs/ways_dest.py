import heapq
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

def ways(n, roads):
    adj_lst = [[] for _ in range(n)]

    for u,v,m in roads:
        adj_lst[u].append([v,m])
        adj_lst[v].append([u,m])

    distance = [float('inf')]*n
    distance[0] = 0
    queue = [(0, 0)]
    paths = [0]*n
    paths[0] = 1

    while queue:
        dst, node = heapq.heappop(queue)

        if dst > distance[node]:
            continue

        for neighbour, time in adj_lst[node]:
            total_dist = dst+time
            if total_dist == distance[neighbour]:
                paths[neighbour] = paths[neighbour] + paths[node]
    
            if distance[neighbour] > total_dist:
                paths[neighbour] = paths[node]
                distance[neighbour] = total_dist
                heapq.heappush(queue, (total_dist, neighbour))
    
    return (paths[n-1]%((10**9)+7))

print(ways(n, roads))
