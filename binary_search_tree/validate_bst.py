
def validate_bst(root):
    prev = None
    current = root

    while current is not None:
        if current.left is None:
            if prev is not None and prev>=current.val:
                return False
            prev = current.val
            current = current.right
        
        else:
            predecessor = current.left

            while predecessor.right is not None and predecessor.right != current:
                predecessor = predecessor.right
            
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                if prev is not None and prev>=current.val:
                    return False
                prev = current.val
                current = current.right

    return True
