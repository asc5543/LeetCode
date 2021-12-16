# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sortRoot = ListNode(head.val)
        head = head.next
        while not head == None:
            sortRoot = self.insertElement(sortRoot, head.val)
            head = head.next
        return sortRoot
        
    def insertElement(self, head, val):
        # insert val to a list
        root = ListNode(0)
        root.next = head
        itr = root
        while not itr.next == None:
            if itr.next.val > val:
                NewNode = ListNode(val)
                NewNode.next = itr.next
                itr.next = NewNode
                return root.next
            else:
                itr = itr.next
        itr.next = ListNode(val)
        return root.next