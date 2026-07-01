V = 4
edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]
src = 0


def bellman_algo(V, edges, src):
    distance = [float('inf')]*V
    distance[src] = 0
    looprun = 0

    for i in range(V+1):
        looprun += 1
        for u, v, w in edges:
            if distance[u] == float('inf'):
                continue
            total_dist = distance[u]+w
            if looprun == V and total_dist < distance[v]:
                return -1
            if total_dist < distance[v]:
                distance[v] = total_dist
        
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i] = 10**8
    return distance

print(bellman_algo(V, edges, src))