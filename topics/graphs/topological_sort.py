V = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]

def topological_sort(edges, V):
    adj_list = [[] for _ in range(V)]

    for u,v in edges:
        adj_list[u].append(v)

    visited = [0]*V
    stack = []

    def dfs(node):
        visited[node] = 1
        for adj_node in adj_list[node]:
            if visited[adj_node] == 0:
                dfs(adj_node)
        stack.append(node)

    for i in range(V):
        if visited[i]==0:
            dfs(i)

    return stack[::-1]

print(topological_sort(edges, V))