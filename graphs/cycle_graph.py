from collections import deque
V = 4
E = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]


# def cycle_bfs(edges, v):
#     adj_list = [[] for _ in range(v) ]

#     for u, w in edges:
#         adj_list[u].append(w)
#         adj_list[w].append(u)

#     visited = [0]*v

#     for i in range(v):
#         if visited[i] == 0:
#             queue = deque([])

#             queue.append((i, -1))
#             visited[i] = 1

#             while queue:
#                 node, parent = queue.popleft()

#                 for neighbour in adj_list[node]:
#                     if visited[neighbour] == 0:
#                         visited[neighbour] = 1
#                         queue.append((neighbour, node))
                    
#                     elif neighbour != parent:
#                         return True
#     return False

# print(cycle_bfs(edges, V))


def cycle_dfs(edges, V):
    adj_list = [[] for _ in range(V)]

    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = [0]*V


    def helper(node, parent, visited, adj_list):
        visited[node] = 1

        for neighbour in adj_list[node]:
            if visited[neighbour] == 0:
                ans = helper(neighbour, node, visited, adj_list)
                if ans == True:
                    return True
            elif neighbour != parent:
                return True
        
        return False
    
    for i in range(V):
        if visited[i] == 1:
            continue
        ans = helper(i, -1, visited, adj_list)
        if ans == True:
            return True
        
    return False


print(cycle_dfs(edges, V))
