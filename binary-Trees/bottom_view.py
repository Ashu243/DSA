from collections import deque
def bottom_view(node):
    queue = deque([])
    result = {}
    queue.append([node, 0])
    while queue:
        elem, line = queue.popleft()
        result[line] = elem.val
        if elem.left:
            queue.append([elem.left, line-1])
        if elem.right:
            queue.append([elem.right, line+1])
        
    ans = []
    for value in sorted(result.items()):
        ans.append(value[1])

    return ans