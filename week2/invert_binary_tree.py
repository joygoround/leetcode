# https://leetcode.com/problems/invert-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # empty root
        if root == None:
            return None

        # create a new root with value of original root
        inverted = TreeNode(val=root.val)
        # iterate nodes and update the new roots with new leaves
        go_through(root, inverted)
        return inverted


def go_through(root, inverted):
    # inset new nodes with switched values
    inverted.left = None if root.right == None else TreeNode(
        val=root.right.val)
    inverted.right = None if root.left == None else TreeNode(val=root.left.val)
    # to next node
    if root.left:
        go_through(root.left, inverted.right)
    if root.right:
        go_through(root.right, inverted.left)
