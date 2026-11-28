# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        def getLeftHeight(node):
            count = 0
            while node:
                count += 1
                node = node.left
            return count
        
        def getRightHeight(node):
            count = 0
            while node:
                count += 1
                node = node.right
            return count
        
        
        def recursion(node):
            lh = getLeftHeight(node)
            rh = getRightHeight(node)
            
            if lh == rh:
                return 2**lh - 1
            return recursion(node.left) + recursion(node.right) + 1
        return recursion(root)
            