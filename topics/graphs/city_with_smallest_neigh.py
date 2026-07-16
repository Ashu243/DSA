n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

def city_with_smallest_neigh(n, edges, dt):
    dist = [[10**5 for _ in range(n)] for _ in range(n)]

    for u,v,w in edges:
        dist[u][v] = w
        dist[v][u] = w

    for i in range(n):
         dist[i][i] = 0

    adj_list = [[] for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != 10**5 and dist[k][j] != 10**5:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    cnt = 0
    result = float('inf')
    ans = 0
    for i in range(n):
         for j in range(n):
              if dt >= dist[i][j]:
                   cnt += 1
         if result >= cnt:
              result = cnt
              ans = i
         cnt = 0
    
    return ans
         

print(city_with_smallest_neigh(n, edges, distanceThreshold))
