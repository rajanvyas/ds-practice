# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return
        if len(preorder) == 1:
            root = TreeNode(preorder[0])
            return root
        root = TreeNode(preorder[0])
        div = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:(div + 1)], inorder[0:div])
        root.right = self.buildTree(preorder[(div + 1):], inorder[(div + 1):])
        return root