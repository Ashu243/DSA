
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(self, head):
    """
    Do not return anything, modify head in-place instead.
    """

    # Step 1: Find the middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev = None
    current = slow

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    # prev is now the head of the reversed second half
    list1 = head
    list2 = prev

    # Step 3: Merge both lists alternately
    dummy = ListNode(0)
    current = dummy
    take_first = True

    while list1 and list2:
        if take_first:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next
        take_first = not take_first