# LC 104 Easy Maximum Depth of Binary Tree
"""
LC 104 Easy; Maximum Depth of Binary Tree


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
keep level order build in mind
Input: root =
        3
       / \
      9   20
         /  \
        15   7
Output: 3

todo: try BFS and iterative DFS also
"""

"""
Time Complexity: O(n)
Space Complexity: O(h) where h = height of tree (worst-case O(n))
    - Balanced tree: height: O(log n) space complexity: O(log n)
    - Skewed tree:   height: O(n) space complexity: O(n)

"""
from binarytree.tree import TreeNode


def max_depth(root: TreeNode):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
