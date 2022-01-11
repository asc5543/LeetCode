# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumRootToLeafOnePath(root, 0)
        
    def sumRootToLeafOnePath(self, root, parent):
        if root == None:
            return 0
        sum = parent*2 + root.val
        if root.left == None and root.right == None:
            return sum
        return self.sumRootToLeafOnePath(root.left, sum) + self.sumRootToLeafOnePath(root.right, sum)