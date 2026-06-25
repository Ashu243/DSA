from collections import deque
graph = [[1,2],[2,3],[5],[0],[5],[],[]]


def safe_states(graph):
    V = len(graph)
    graph_rev = [[] for _ in range(V)]

    indegrees = [0]*V

    for i in range(V):
        for j in graph[i]:
            graph_rev[j].append(i)
            indegrees[i] += 1

    queue = deque([])
    result = []

    for i in range(V):
        if indegrees[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour in graph_rev[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
    
    result.sort()
    return result
    

print(safe_states(graph))