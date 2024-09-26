# Closest Binary Search Tree Value


"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
If there are multiple answers, print the smallest.


Example 1:

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:

Input: root = [1], target = 4.428571
Output: 1


Constraints:

    The number of nodes in the tree is in the range [1, 104].
    0 <= Node.val <= 109
    -109 <= target <= 109

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        current = root

        while current:
            # Update closest if current value is closer to target
            if abs(current.val - target) < abs(closest - target):
                closest = current.val
            elif abs(current.val - target) == abs(closest - target):
                # If distances are equal, choose the smaller value
                closest = min(current.val, closest)

            if target < current.val:
                current = current.left
            elif target > current.val:
                current = current.right
            else:
                # If we find an exact match, we can return immediately
                return current.val

        return closest