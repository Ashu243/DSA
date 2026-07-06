V = 7
edges = [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]


def connected_component(V, edges):
    parent = [n for n in range(V)]
    rank = [0 for _ in range(V)]

    def find(node):
        if node == parent[node]:
            return node
        
        parent[node] = find(parent[node])
        return parent[node]
    
    parent_set = set()
    for u,v in edges:
        x = find(u)
        y = find(v)

        if rank[x] > rank[y]:
            parent[y] = x

        elif rank[y] > rank[x]:
            parent[x] = y

        
        else:
            parent[y] = x
            rank[x] += 1
    
    for i in parent:
        parent_set.add(find(i))

    return len(parent_set)


print(connected_component(V, edges))