V = 3
E = 3
edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]


def kruskal_algo(V, edges):
    edges.sort(key=lambda edge: edge[2])

    parent = [n for n in range(V)]
    rank = [0 for _ in range(V)]

    total_weight = 0

    def find(node):
        if node == parent[node]:
            return node
        parent[node] = find(parent[node])
        return parent[node]

    for u, v, w in edges:
        x = find(u)
        y = find(v)

        if x == y:
            continue

        if rank[x] > rank[y]:
            parent[y] = x
        
        elif rank[y] > rank[x]:
            parent[x] = y
        
        else: 
            parent[y] = x
            rank[x] += 1
        total_weight += w

    return total_weight 

print(kruskal_algo(V, edges))