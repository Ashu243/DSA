# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        carry = 0
        newNode = dummy

        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            new_val = val1 + val2 + carry

            newNode.next = ListNode(new_val%10)

            carry = new_val // 10

            newNode = newNode.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return dummy.next
        
