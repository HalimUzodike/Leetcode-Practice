# Binary Trees

"""
Like a linked list, a tree is a type of graph. Also like a linked list, there are multiple types of trees.
In this course, we will be focusing on binary trees. Let's take a look at what a binary tree is.




Tree terminology

There is some tree-specific terminology that you will need to learn.

The root node is the node at the "top" of the tree. Every node in the tree is accessible starting from the root node.
In most tree questions, the root of the tree will be given as the input, just like how in linked lists, the head was given as the input.

If you have a node A with an edge to a node B, so A -> B, we call A the parent of node B, and node B a child of node A.

If a node has no children, it is called a leaf node. The leaf nodes are the leaves of the tree.

The depth of a node is how far it is from the root node. The root has a depth of 0.
Every child has a depth of parentsDepth + 1, so the root's children have a depth of 1, their children have a depth of 2, and so on.



class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""






#


