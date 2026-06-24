V = 4
edges = edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 3]
]

def cycle(edges, V):
    adj_list = [[] for _ in range(V)]

    for u,v in edges:
        adj_list[u].append(v)

    visited = [0]*V
    path_visited = [-2]*V
    found = False

    def dfs(node):
        visited[node] = 1
        path_visited[node] = 1
        for neighbour in adj_list[node]:
            if path_visited[neighbour] == 1:
                return True
            elif visited[neighbour] == 0:
                if dfs(neighbour):
                    return True
        path_visited[node] = 0
        return False

    for i in range(V):
        if visited[i] == 0:
            ans = dfs(i)
            if ans == True:
                found = True
                break
    
    return found

print(cycle(edges, V))