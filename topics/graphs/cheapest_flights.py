from collections import deque
n = 5
flights = [[1,0,5],[2,1,5],[3,0,2],[1,3,2],[4,1,1],[2,4,1]]
src = 2
dst = 0
k = 2


# getting TLE Error
# def cheapest_flights(n, flights, src, dst, k):
#     adj_list = [[] for _ in range(n)]

#     for u,v,p in flights:
#         adj_list[u].append([v,p])

#     if adj_list[src] == []:
#         return -1
    
#     price_lst = [float('inf')]*n
#     price_lst[src] = 0

#     queue = [(0, src, 0)]

#     while queue:
#         cost, node, stop_used = heapq.heappop(queue)
#         if stop_used > k+1:
#             continue
#         if node == dst:
#              return cost

#         for neighbour, price in adj_list[node]:
#                 total_price = price + cost
#                 new_stop = stop_used + 1
#                 heapq.heappush(queue, (total_price, neighbour, new_stop))

#     return -1

def cheapest_flights(n, flights, src, dst, k):
    adj_list = [[] for _ in range(n)]

    for u,v,p in flights:
        adj_list[u].append([v,p])

    if adj_list[src] == []:
        return -1
    
    price_lst = [float('inf')]*n
    price_lst[src] = 0

    queue = deque([])
    queue.append([0, src, 0])

    while queue:
        steps, node, cost = queue.popleft()

        if steps > k:
            continue

        for neighbour, price in adj_list[node]:
            new_cost = cost + price

            if new_cost < price_lst[neighbour]:
                price_lst[neighbour] = new_cost
                queue.append((steps + 1, neighbour, new_cost))

    if price_lst[dst] == float('inf'):
        return -1
    return price_lst[dst]


print(cheapest_flights(n, flights, src, dst, k))