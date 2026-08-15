# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0)
        dummy.next = head
        current = head
        beforeNode = dummy

        while current:
            temp = current
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1
            
            if count < k:
                break

            count = 0
            startingNode = current
            prev = None
            while count < k:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
                count += 1
            
            beforeNode.next = prev
            beforeNode = startingNode
            startingNode.next = current
        
        return dummy.next
