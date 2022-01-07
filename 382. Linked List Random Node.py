# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.NodeValue = []
        while head:
            self.NodeValue.append(head.val)
            head = head.next

    def getRandom(self):
        """
        :rtype: int
        """
        import random
        index = random.randint(0, len(self.NodeValue)-1)
        return self.NodeValue[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()