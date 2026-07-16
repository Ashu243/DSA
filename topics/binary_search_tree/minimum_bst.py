"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        # code here
        temp = root
        result = -1
        while temp is not None:
            result = temp.data
            temp = temp.left
        
        return result