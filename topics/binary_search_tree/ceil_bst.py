'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        temp = root
        result = -1
        while temp is not None:
            if temp.data == x:
                return x
            
            elif temp.data > x:
                result = temp.data
                temp = temp.left
            
            else:
                temp = temp.right
        
        return result
                
            
        