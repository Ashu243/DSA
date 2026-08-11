

def reverse_ll(head):
    current = head
    previousNode = None
    while current:
        next_node = current.next
        current.next = previousNode
        previousNode = current
        current = next_node
    return previousNode