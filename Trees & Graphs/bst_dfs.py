"""
DFS

In a DFS, we prioritize depth by traversing as far down the tree as possible in one direction (until reaching a leaf node) before considering the other direction.
For example, let's say we choose left as our priority direction. We move exclusively with node.left until the left subtree has been fully explored.
Then, we explore the right subtree.

Trees are named as such because they resemble real-life trees.
You can think of the paths of a binary tree as branches growing from the root.
DFS chooses a branch and goes as far down as possible. Once it fully explores the branch, it backtracks until it finds another unexplored branch.

Because we need to backtrack up the tree after reaching the end of a branch,
DFS is typically implemented using recursion, although it is also sometimes done iteratively using a stack.
Here is a simple example of recursive DFS to visit every node:

    Each call to dfs(node) is visiting that node. As you can see in the code, we visit the left child before visiting the right child.

def dfs(node):
    if node == None:
        return

    dfs(node.left)
    dfs(node.right)
    return
"""


# Minimum Depth of Binary Tree

"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#
#         if not root:
#             return 0
#
#         if root.left and root.right:
#             return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
#
#         if root.left:
#             return self.minDepth(root.left) + 1
#
#         if root.right:
#             return self.minDepth(root.right) + 1
#
#         else:
#             return 1


# Better solution

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # If the node has no left child, recurse on the right child
        elif not root.left:
            return self.minDepth(root.right) + 1

        # If the node has no right child, recurse on the left child
        elif not root.right:
            return self.minDepth(root.left) + 1

        # If the node has both children, take the minimum of the two depths
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1


"""
Iterative Solution

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop(0)

            # If we find a leaf node, return its depth immediately
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0  # This line will never be reached for valid binary trees
"""



# Maximum Depth of Binary Tree

"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#
#         if not root:
#             return 0
#
#         if root.left and root.right:
#             return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
#
#         if root.left:
#             return self.maxDepth(root.left) + 1
#
#         if root.right:
#             return self.maxDepth(root.right) + 1
#
#         else:
#             return 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


"""
Iterative Solution

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        ans = 0

        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return ans
"""