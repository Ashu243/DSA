from collections import deque
def right_view(node):
    queue = deque([])
    line = 0
    queue.append([node, line])
    result = {}
    while queue:
        elem, line = queue.popleft()
        if line not in result:
            result[line] = elem
        line += 1
        if elem.right:
            queue.append([elem.right, line])
        if elem.left:
            queue.append([elem.left, line])
    
    ans = []
    for value in sorted(result.items()):
        ans.append(value[1])

    return ans