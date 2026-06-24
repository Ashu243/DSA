from collections import deque
V = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]

def topological_sort_kahn(edges, V):
    adj_list = [[] for _ in range(V)]

    indegrees = [0]*V

    for u, v in edges:
        adj_list[u].append(v)
        indegrees[v] += 1
    
    queue = deque([])

    for i in range(V):
        if indegrees[i] == 0:
            queue.append(i)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbour in adj_list[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
    
    return result

print(topological_sort_kahn(edges, V))