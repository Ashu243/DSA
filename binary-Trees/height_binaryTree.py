from collections import deque

def height(root):
    queue = deque([])
    height = 0
    queue.append(root)
    while queue:
        size = len(queue)
        height += 1

        for _ in range(size):
            e = queue.popleft()
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
    
    return height