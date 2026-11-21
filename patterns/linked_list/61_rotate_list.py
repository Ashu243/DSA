# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        dummy = ListNode(0)
        slow = head
        fast = head
        count = 1

        while fast.next:
            fast = fast.next
            count += 1
        fast = head
        loop_run = k % count

        if loop_run == 0:
            return head

        for _ in range(loop_run):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        dummy.next = slow.next
        fast.next = head
        slow.next = None
        return dummy.next