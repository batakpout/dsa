# LC 102. medium.  Binary Tree Level Order Traversal

"""

        1
      /   \
     2     3
    / \   / \
   4  5  6   7

   output = [[1], [2,3], [4,5,6,7]]
"""

"""
Python lists are great for appending to the end: e.g list.append(1), list.pop() are O(1) operations, But adding or 
removing from the front of a list is slow because all the remaining elements must shift:
A deque performs these operations in O(1) time.
Almost every BFS solution on LeetCode uses a deque: here level order traversal is also BFS
"""

"""
Time : O(n) Each node is visited exactly once.
       Even though there is a nested for loop inside the while loop, the total number of iterations of the for loop
        across the entire execution is exactly n (one iteration per node).
Space: O(n)

The queue O(n/2), current level O(n) , and result O(n) together store at most O(n) node references.
"""
from binarytree.tree import TreeNode
from collections import deque


def level_order_traversal(root: TreeNode):
    dq = deque()
    result = []
    dq.append(root)
    while dq:
        level = []
        for _ in range(len(dq)):
            node = dq.popleft()
            level.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        result.append(level)

    return result
