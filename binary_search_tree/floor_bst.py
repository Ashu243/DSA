'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        temp = root
        result = -1
        while temp is not None:
            if temp.data == k:
                return k
            
            elif temp.data > k:
                temp = temp.left
            
            else:
                result = temp.data
                temp = temp.right
        
        return result