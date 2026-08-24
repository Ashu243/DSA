from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, node):
        root = node
        def recursion(node):
            if node is None:
                return
            
            node.left, node.right = node.right, node.left
            recursion(node.left)
            recursion(node.right)
        recursion(node)
        return root

        