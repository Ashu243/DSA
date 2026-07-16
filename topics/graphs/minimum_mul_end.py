from collections import deque
arr = [3, 4, 65]
start = 7
end = 175

def mini_end(arr, start, end):

    queue = deque([])
    visited = set()

    queue.append((0, start))
    visited.add(start)

    while queue:
        count, node = queue.popleft()
        if end == node:
            return count

        for i in range(len(arr)):
            result = (node*arr[i])%1000
            if result in visited:
                continue
            visited.add(result)
            queue.append((count+1, result))
            
    return -1


print(mini_end(arr, start, end))