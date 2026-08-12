# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         val = val
#         next = next
class Solution:
    def removeNthNode(self, head, n):
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return head
