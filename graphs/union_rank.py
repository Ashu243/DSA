n = 5
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

# def find(node):
#     if node == parent[node]:
#         return node
    
#     parent[node] = find(parent[node])
#     return parent[node]


# def union(x, y):
#     u = find(x)
#     v = find(y)

#     if u == v:
#         return

#     if rank[u] > rank[v]:
#         parent[v] = u

#     elif rank[u] < rank[v]:
#         parent[u] = v

#     else:
#         parent[v] = u
#         rank[u] += 1
    
size = [1 for _ in range(n+1)]

def findParent(node):
    if node == parent[node]:
        return node
    
    parent[node] = findParent(parent[node])
    return parent[node]

def union(x, y):
    u = findParent(x)
    v = findParent(y)

    if u == v:
        return 
    
    elif size[u] > size[v]:
        size[u]+= size[v]
        parent[v] = u
    
    elif size[v] > size[u]:
        size[v]+= size[u]
        parent[u] = v

    else:
        parent[v] = u
        size[u]+= size[v]