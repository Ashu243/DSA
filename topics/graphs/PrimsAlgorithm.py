import heapq
V = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]

def prims_algo(v, edges):
    adj_list = [[] for _ in range(v)]

    for u,v,w in edges:
        adj_list[u].append([v,w])
        adj_list[v].append([u,w])

    # print(adj_list)

    result = 0
    visited = [0]*V

    queue = [(0, 0, -1)]

    while queue:
        wt, node, parent = heapq.heappop(queue)

        if visited[node] == 1:
            continue
        result = result+wt

        visited[node] = 1

        for neighbour, weight in adj_list[node]:
            if visited[neighbour] == 0:
                heapq.heappush(queue, (weight, neighbour, node))
    
    return result

print(prims_algo(V, Edges))