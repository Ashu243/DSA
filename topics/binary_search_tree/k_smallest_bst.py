
k = 3
root = 1
def kth_smallest(k):

    result = 0
    current = root

    while current is not None:
        if current.left is None:
            k -= 1
            if k == 0:
                result = current.val
            current = current.right
        
        else:
            pred = current.left
            while pred.right is not None and pred.right != current:
                pred = pred.right

            if pred.right is None:
                pred.right = current
                current = current.left
            else:
                pred.right = None
                k -= 1
                if k == 0:
                    result = current.val
                current = current.right
    return result
