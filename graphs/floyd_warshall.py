dist = [[0, 4, 10**8, 5, 10**8], [10**8, 0, 1, 10**8, 6], [2, 10**8, 0, 3, 10**8], [10**8, 10**8, 1, 0, 2], [1, 10**8, 10**8, 4, 0]]


def floyd_warshall(dist):
    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != 10**8 and dist[k][j] != 10**8:
                    dist[i][j] = min(dist[i][j], (dist[i][k]+dist[k][j]))


    return dist

print(floyd_warshall(dist))
