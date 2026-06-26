from collections import deque
V = 9
edges = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]]
src = 0


def shortest_path(edges, V, src):
    adj_list = [[] for _ in range(V)]

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # visited = [0]*V
    distance = [-1]*V

    queue = deque([])
    queue.append(src)
    # visited[src] = 1
    distance[src] = 0

    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[node]+1
                # visited[neighbour] = 1
                queue.append(neighbour)

    return distance

print(shortest_path(edges, V, src))




