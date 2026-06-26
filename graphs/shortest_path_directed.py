from collections import deque
V = 4
E = 7
edges = [[0,1,2], [0,2,1]]

def shortest_dir_path(edges, V, E):
    adj_list = [[] for _ in range(V)]

    for u, v, w in edges:
        adj_list[u].append([v, w])

    distance = [float('inf')]*V

    queue = deque([])
    queue.append(0)
    distance[0] = 0

    while queue:
        node = queue.popleft()
        for neighbour, dist in adj_list[node]:
            if distance[node] + dist < distance[neighbour]:
                distance[neighbour] = dist + distance[node]
                queue.append(neighbour)
    
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i] = -1
    
    return distance


print(shortest_dir_path(edges, V, E))