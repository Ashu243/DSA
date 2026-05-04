from collections import deque

n = 9
adj_list = [
    [],
    [2, 8],
    [1,3,4],
    [2],
    [2,5],
    [4,6],
    [5,7],
    [6,8],
    [1,7,9],
    [8],
]

def bfs_traversal(adj, starting_node):
    queue = deque([])

    queue.append(starting_node)
    visited = set()
    visited.add(starting_node)
    result = []
    while queue:
        elem = queue.popleft()
        result.append(elem)
        for node in adj[elem]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
    return result

print(bfs_traversal(adj_list, 1))

# def dfs_traversal(adj, node, visited, result):
#     visited.add(node)
#     result.append(node)

#     for i in adj[node]:
#         if i not in visited:
#             dfs_traversal(adj, i, visited, result)

# visited = set()
# result = []

# dfs_traversal(adj_list, 1, visited, result)

# print(result)