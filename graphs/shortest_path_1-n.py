import heapq
n = 5
m = 6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]


def shortest_path(edges, n):
    if len(edges) == 0:
        return [-1]
    adj_list = [[] for _ in range(n+1)]

    for u,v,d in edges:
        adj_list[u].append([v,d])
        adj_list[v].append([u,d])

    distance = [float('inf')]*(n+1)
    parent = [i for i in range(n+1)]

    distance[1] = 0
    priority_queue = [[0, 1]]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if dist > distance[node]:
            continue
        for neighbour, weight in adj_list[node]:
            total_distance = weight+distance[node]
            if distance[neighbour] > total_distance:
                distance[neighbour] = total_distance
                parent[neighbour] = node
                heapq.heappush(priority_queue, (total_distance, neighbour))

    if distance[n] == float('inf'):
        return [-1]

    result = []
    original_n = n
    while parent[n] != n:
        result.append(n)
        n = parent[n]
    result.append(1)
    result.append(distance[original_n])
    result.reverse()

    return result


print(shortest_path(edges, n))