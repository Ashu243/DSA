# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        curr = head

        # the node to return
        ans = head.next
        prev = None
        while curr and curr.next:
            nextNode = curr.next
            nextpair = curr.next.next

            # swap the nodes
            nextNode.next = curr
            curr.next = nextpair

            # connect the last node to the first node after swapping
            if prev:
                prev.next = nextNode
            
            prev = curr
            curr = curr.next
        
        return ans
        