# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples 1:
#
# Input: [3,9,20,null,null,15,7]
#
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
#
# Output:
#
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:
#
# Input: [3,9,8,4,0,1,7]
#
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#
# Output:
#
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:
#
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
#
# Output:
#
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        q = []

        node = root
        q.append([node, 0])

        output = {}

        while len(q) > 0:
            node, level = q.pop(0)

            if not (level in output):
                output[level] = [node.val]
            else:
                output[level].append(node.val)

            if node.left is not None:
                q.append([node.left, level - 1])
            if node.right is not None:
                q.append([node.right, level + 1])

        sortedkeys = sorted(output.keys())
        vertorder = []
        for i in sortedkeys:
            vertorder.append(output[i])
        return vertorder