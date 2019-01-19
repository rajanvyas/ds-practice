# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.path(root, '', res)
        return res

    def path(self, root, string, res):

        string += str(root.val)

        if root.left:
            self.path(root.left, string + '->', res)

        if root.right:
            self.path(root.right, string + '->', res)

        if not root.left and not root.right:
            res.append(string)
