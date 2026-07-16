n = 12
connections = [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]

def computer_network(n, connections):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(node):
        if node == parent[node]:
            return node
        parent[node] = find(parent[node])
        return parent[node]
    
    edges = 0
    total_component = set()
    
    for u, v in connections:
        x = find(u)
        y = find(v)

        if x == y:
            edges += 1

        if rank[x] > rank[y]:
            parent[y] = x

        elif rank[y] > rank[x]:
            parent[x] = y
        
        else:
            parent[y] = x
            rank[x] += 1

    for i in parent:
        total_component.add(find(i))

    required_connection = (len(total_component)-1)
    print(required_connection, edges)

    if required_connection <= edges:
        return required_connection % (edges+1)
        # return required_connection - could simply write like this but my mind was crazy!
    
    
    return -1

print(computer_network(n, connections))
        


