from collections import deque
def top_view(node):
    queue = deque([])
    result = {}
    queue.append([node, 0])
    while queue:
        elem, line = queue.popleft()
        if line not in result:
            result[line] = elem.val
        if elem.left:
            queue.append([elem.left, line-1])
        if elem.right:
            queue.append(elem.right, line+1)
    ans = []
    for value in sorted(result.values()):
        ans.append(value)
    return ans