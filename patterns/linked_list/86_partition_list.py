# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        current = head
        lessDummy = ListNode(0)
        greaterDummy = ListNode(0)

        less = lessDummy
        greater = greaterDummy

        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next

            current = current.next
        
        greater.next = None
        less.next = greaterDummy.next
        return lessDummy.next



        