# Maximum Difference Between Node Ancestors

"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3


Constraints:

    The number of nodes in the tree is in the range [2, 5000].
    0 <= Node.val <= 105

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Use helper function
        # As this is a BST then every val to left of root is less and val on right is more
        # Find max diff on each side
        # Find max diff between both sides
        # we will track the max val and min val
        # Each time we will find the diff between the current max and min
        # We will also store the max result
        # Return the max result

        if not root:
            return 0

        def helper(node, curr_max, curr_min):

            if not node:
                return abs(curr_max - curr_min)

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            left = helper(node.left, curr_max, curr_min)
            right = helper(node.right, curr_max, curr_min)

            return max(left, right)
        return helper(root, root.val, root.val)

