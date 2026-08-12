# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# intuition
# find the mid
# reverse the after mid part
# compare both the halves
class Solution:
    def isPalindrome(self, head):
        if not head.next:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        p1 = head
        current = prev
        while current and p1:
            if current.val != p1.val:
                return False
            current = current.next
            p1 = p1.next
        return True