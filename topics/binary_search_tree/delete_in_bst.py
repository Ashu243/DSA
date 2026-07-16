
def delete_node_bst(root, key):
    if root is None:
        return None

    def lstchild(node):
        while node.right is not None:
            node = node.right
        return node

    def delete_node(node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        else:
            right_child = node.right
            last_rc = lstchild(node.left)
            last_rc.right = right_child
            return node.left
    
    if root.val == key:
        root = delete_node(root)
        return root
    temp = root

    

    while temp is not None:
        if temp.val > key:
            if temp.left is not None and temp.left.val == key:
                temp.left = delete_node(temp.left)
                break
            else:
                temp = temp.left
        
        elif temp.val < key:
            if temp.right is not None and temp.right.val == key:
                temp.right = delete_node(temp.right)
                break
            
            else:
                temp = temp.right
    
    return root