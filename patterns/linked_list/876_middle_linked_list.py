

def middle_linked_list(head):
    fast = head
    slow = head
    while fast:
        fast = fast.next.next
        slow = slow.next
    return slow