
def max_diameter(node):
    diameter = 0

    def height(node):
        if node == None:
            return 0
        
        left = height(node.left)
        right = height(node.right)
        diameter = max(diameter, left+right)
        return 1 + max(left, right)