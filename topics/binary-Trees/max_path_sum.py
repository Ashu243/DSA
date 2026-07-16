maxi = float('-inf')
node = 0
def max_path_sum(node):
    if node == None:
        return 0
    left = max(0, max_path_sum(node.left))
    right = max(0, max_path_sum(node.right))
    maxi = max(maxi, right+left+node.val)
    return node.val + max(left, right)
max_path_sum(node)
        