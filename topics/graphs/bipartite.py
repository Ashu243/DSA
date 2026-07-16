from collections import deque
graph = [[1,3],[0,2],[1,3],[0,2]]

def bipartite(graph):
    v = len(graph)
    visited = [-1]*v
    
    queue = deque([])

    for i in range(v):
        if visited[i] != -1:
            continue
        visited[i] = 0
        queue.append((i, 0))

        while queue:
            node, color = queue.popleft()

            for neighbour in graph[node]:
                if visited[neighbour] == -1:
                    if color == 0:
                        visited[neighbour] = 1
                        queue.append((neighbour, 1))
                    else:
                        visited[neighbour] = 0
                        queue.append((neighbour, 0))

                elif visited[neighbour] == color:
                    return False
                
    return True

print(bipartite(graph))


