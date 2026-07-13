"""
 //DFS: pre,post,in order traversal
 //DFS:I’ll go as deep as possible in one direction before I backtrack

 /*
        1
       / \
      2   3
     / \  / \
    4  5 6   7

Traversal Outputs:

Pre-order (Root → Left → Right):
1 2 4 5 3 6 7

In-order (Left → Root → Right):
4 2 5 1 6 3 7

Post-order (Left → Right → Root):
4 5 2 6 7 3 1

Level-order
1 2 3 4 5 6 7
 */

"""

# LC 94  easy binary tree inorder   traversal
# LC 144 easy binary tree preorder traversal
# LC 145 easy binary tree postorder traversal


from binarytree.tree import TreeNode
from typing import Optional

"""
It is DFS (Depth-First Search) I’ll go as deep as possible in one direction before I backtrack
Time: O(N) each node is visited once and appended exactly once
Space:
Memory Used         | Balanced Tree | Skewed Tree

Result list         | O(n)          | O(n)

Recursion stack     | O(log n)      | O(n)
----------------------------------------------------
Total space         | O(n)          | O(n)
----------------------------------------------------
Auxiliary space     | O(log n)      | O(n)
(excluding result)

"""


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result = []

    def inorder(root):
        if not root:
            return result
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)

    inorder(root)
    return result


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result = []

    def pre_order(root):
        if not root:
            return result
        result.append(root.val)
        pre_order(root.left)
        pre_order(root.right)

    pre_order(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result = []

    def postorder(root):
        if not root:
            return result
        postorder(root.left)
        postorder(root.right)
        result.append(root.val)

    postorder(root)
    return result

"""
 for iterative solutions:
Time = O(N) 
Space = O(h) where h is the height of the tree.

This is more precise because:

* Balanced tree: h = log(n), so space is O(log n).
* Completely skewed tree: h = n, so O(h) = O(n).
* O(h) is auxillary space. Total is O(n) for result list + O(h) = O(N)
* most people bother only about auxillary space, Because they are referring to the auxiliary space, i.e.,
  the extra working memory used by the algorithm excluding the output.
"""

"""
Algorithm

1. Push root.
2. Pop node.
3. Visit it.
4. Push right child.
5. Push left child.
6. Repeat.
"""
def preorder_iterative(root: Optional[TreeNode]):
    result = []
    if root is None:
        return result
    stack = [root]
    while stack:
        curr = stack.pop()
        result.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result

"""
while current or stack:
    go left while possible
    pop
    visit
    go right
"""
def inorder_iterative(root: Optional[TreeNode]):
    result = []
    stack = []
    curr: TreeNode = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right


"""
A node can only be visited after both children are done.
So keep track of the last node that was visited.
"""
def postorder_iterative(root: Optional[TreeNode]):
    result=[]
    if not root:
        return result
    last_visited=None
    stack=[]
    curr=root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.left
        peek = stack[-1]
        if peek.right and peek.right != last_visited:
            curr = peek.right
        else:
            result.append(peek.val)
            last_visited = stack.pop()

    return result

