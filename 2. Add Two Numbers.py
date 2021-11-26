# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        listNodeSum = ListNode()
        head = listNodeSum
        pointer = listNodeSum
        intCarry = 0
        while not l1 == None and not l2 == None:
            intTemp = (l1.val + l2.val + intCarry) % 10
            intCarry = (l1.val + l2.val + intCarry) // 10
            pointer.next = ListNode(intTemp)
            pointer = pointer.next
            l1 = l1.next
            l2 = l2.next
            
        # l1 has remain value
        while not l1 == None:
            intTemp = (l1.val + intCarry) % 10
            intCarry = (l1.val + intCarry) // 10
            pointer.next = ListNode(intTemp)
            pointer = pointer.next
            l1 = l1.next    
            
        # l2 has remain value
        while not l2 == None:
            intTemp = (l2.val + intCarry) % 10
            intCarry = (l2.val + intCarry) // 10
            pointer.next = ListNode(intTemp)
            pointer = pointer.next
            l2 = l2.next   
            
        # intCarry not zero
        if intCarry == 1:
            pointer.next = ListNode(intCarry)
            
        return head.next