import heapq
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

def dijkstra(edges, V, src):
    adj_list = [[] for _ in range(V)]

    for u,v,w in edges:
        adj_list[u].append([v,w])
        adj_list[v].append([u,w])

    print(adj_list)

    distance = [float('inf')]*V
    distance[src] = 0

    priority_queue = [[0, src]]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if dist > distance[node]:
            continue
        for neighbour, weight in adj_list[node]:
            total_dist = dist+weight
            if distance[neighbour] > total_dist:
                distance[neighbour] = total_dist
                heapq.heappush(priority_queue, (total_dist, neighbour))

    return distance


print(dijkstra(edges, V, src))
