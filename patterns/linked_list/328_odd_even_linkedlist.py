class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        # put a pointer odd on first node and even on second node
        odd = head
        even = head.next
        even_head = head.next

        # connect odd nodes with odd and even nodes in even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        # point the last node of odd to the first node of even
        odd.next = even_head

        return head
