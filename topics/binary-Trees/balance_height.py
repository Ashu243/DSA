
def balance_height(node):
    if node == None:
        return 0
    left = balance_height(node.left)
    if left == -1:
        return -1
    right = balance_height(node.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return 1 + max(left, right)
