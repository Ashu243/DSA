# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        current = head
        count = 1
        prevNode = None
        prevleft = None
        while count < left:
            prevleft = current
            current = current.next
            count += 1

        leftnode = current

        while count <= right:
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode
            count += 1

        if prevleft:
            prevleft.next = prevNode
        else:
            head = prevNode
        leftnode.next = current

        return head

        