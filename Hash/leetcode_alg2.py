class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        nextVal = 0
        head = ListNode()
        prevNode = head
        curNode = None

        while l1 or l2:
            nextVal = 0
            l1Val = 0
            l2Val = 0

            if l1:
                l1Val = l1.val
            else:
                l1Val = 0
            if l2:
                l2Val = l2.val
            else:
                l2Val = 0

            nextVal = l1Val + l2Val
            
            if carry == True:
                nextVal += 1
                carry = False

            if nextVal >= 10:
                carry = True
                nextVal -= 10
            
            curNode = ListNode()
            curNode.val = nextVal
            curNode.next = None

            prevNode.next = curNode

            prevNode = curNode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == True:
            curNode = ListNode()
            curNode.val = 1
            curNode.next = None

            prevNode.next = curNode
            prevNode = curNode

        return head.next