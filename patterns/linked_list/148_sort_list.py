# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge_ll(self, l1, l2):
        dummy = ListNode(0)
        prev = dummy
        curr1 = l1
        curr2 = l2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                curr2 = curr2.next
            prev = prev.next
        if curr1:
            prev.next = curr1
        elif curr2:
            prev.next = curr2
        return dummy.next


    def sortList(self, head):
        if not head or head.next is None:
            return head
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge_ll(left, right)