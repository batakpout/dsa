"""
 Dynamic Programming (dp) is a technique for solving problems by breaking them into smaller subproblems, solving
 each subproblem only once, and resuing the result whenever it's needed again

 DP is useful when a problem has two properties:
 1. Overlapping subproblems:
    - The same subproblem is solved multiple times
    - DP avoids repeating that work
2.  Optimal substructure
    - A solution to a large problem can be built from solutions to smaller subproblems

Two Approaches to DP:
    there are two main ways to implement DP:
    1. Top-Down (Memoization)
    2. Bottom-Up (Tabulation)
    They solve the same problem but in opposite directions.

1. Top-down:
    - Idea

    Start with the original problem.
    Whenever you need the answer to a smaller subproblem:

    * Check whether you’ve already solved it.
    * If yes, return the stored answer.
    * Otherwise, solve it, store it, and return it.

    The recursion naturally decides which subproblems are actually needed.

    Characteristics

        * Recursive
        * Uses a cache (dictionary, array, etc.)
        * Computes only the required subproblems

    Mental Model
        Need answer for Problem(10)

            ↓
        Need Problem(9)

            ↓
        Need Problem(8)

            ↓

            ...

        Eventually reach base case.

        Then return upward while remembering every answer.
Advantages

        * Easy to write from recursive solutions.
        * Computes only necessary states.

Disadvantages

        * Uses recursion (possible stack overflow for very deep recursion).
        * Slight recursion overhead.

2. Bottom-Up (Tabulation)

Idea

        Start with the smallest subproblems (base cases).

        Gradually build larger solutions until reaching the final answer.

        Instead of asking:

        “What do I need?”

        you ask:

        “What can I compute next?”

Characteristics

        * Iterative
        * Usually uses a table (dp array)
        * Computes all states in order

Mental Model
        Base cases

            ↓

        Solve Problem(2)

            ↓

        Solve Problem(3)

            ↓

        Solve Problem(4)

            ↓

         ...

            ↓

        Solve Problem(n)
Advantages

    * No recursion.
    * Usually faster due to no recursive calls.
    * Can often be optimized to constant space.

Disadvantages

    * Sometimes computes states that are never actually needed.
    * Requires figuring out the correct computation order.
---------------------------------------------------------------------------
Memoization (Top-Down)           || Tabulation (Bottom-Up)

Recursive                        ||  Iterative

Starts from the final problem    ||  Starts from the smallest problems

Uses a cache                     ||  Uses a DP table

Computes only needed states      ||  Usually computes every state

Easier to derive from recursion  || Often easier to optimize
---------------------------------------------------------------------------

How to Recognize a DP Problem

Ask yourself:

    1. Can I define the problem in terms of smaller versions of itself?

    For example:
        Answer(n)
        depends on

        Answer(n-1)
        Answer(n-2)
        ...
    2. Will I compute the same subproblem multiple times?

        If yes, memoization or tabulation may help.


    3. Can I store previous answers and reuse them?

        If yes, it’s a strong indicator for DP.
 ---------------------------------------------------------------------------
General Steps for Solving DP Problems

    Top-Down

    1. Define the recursive relationship.
    2. Identify the base cases.
    3. Add a cache.
    4. Before solving a subproblem, check the cache.
    5. Store newly computed answers.

⸻

    Bottom-Up

    1. Decide what dp[i] represents.
    2. Initialize the base cases.
    3. Determine the order in which states should be computed.
    4. Fill the table using previously computed values.
    5. Return the final state.
  ---------------------------------------------------------------------------
    Which Should You Choose?

        A good rule of thumb is:

        * If the recursive solution is obvious, start with Top-Down (Memoization). It’s often easier to implement
            and reason about.
        * If recursion depth is a concern or you want the most efficient implementation, use Bottom-Up (Tabulation).
          It avoids recursion and can often be optimized to use O(1) extra space when each state depends on only a few previous states.
Many experienced programmers derive the recurrence recursively (top-down thinking) and then convert it into an iterative
bottom-up solution for better performance. That’s why it’s valuable to understand both approaches—they’re two different
 implementations of the same underlying dynamic programming idea.
"""

######
"""
 # ============================================================
# Dynamic Programming vs Recursion
# ============================================================
#
# Key Idea:
#
# Not every recursive problem should or can benefit from Dynamic
# Programming (DP).
#
# DP is NOT a replacement for recursion.
# DP is an optimization that applies only when a recursive problem
# has specific properties.
#
#
# ------------------------------------------------------------
# Every DP problem can be written recursively...
# ------------------------------------------------------------
#
# Every DP problem starts with a recursive definition.
#
# Example:
#
#     fib(n)
#     = fib(n-1) + fib(n-2)
#
# or
#
#     minCost(i)
#     = cost[i] + min(minCost(i+1), minCost(i+2))
#
# So recursion is usually the starting point.
#
#
# ------------------------------------------------------------
# ...but not every recursive problem is a DP problem.
# ------------------------------------------------------------
#
# The key question is:
#
#     "Do I solve the same subproblem multiple times?"
#
# If YES:
#     DP can help.
#
# If NO:
#     DP usually doesn't help.
#
#
# ------------------------------------------------------------
# Example 1: DP helps
# ------------------------------------------------------------
#
# Fibonacci:
#
#             fib(5)
#            /      \
#        fib(4)    fib(3)
#        /   \      /   \
#    fib(3) fib(2) fib(2)
#
# Notice:
#
#     fib(3)
#
# is computed more than once.
#
# There are repeated (overlapping) subproblems.
#
# ✔ DP is useful.
#
#
# ------------------------------------------------------------
# Example 2: Binary Tree Traversal
# ------------------------------------------------------------
#
#     dfs(node):
#         dfs(node.left)
#         dfs(node.right)
#
# Every node is visited exactly once.
#
# No repeated work.
#
# Adding memoization would do nothing.
#
# ✘ DP is unnecessary.
#
#
# ------------------------------------------------------------
# Example 3: Merge Sort
# ------------------------------------------------------------
#
# sort(left half)
# sort(right half)
# merge
#
# The left and right halves are different.
#
# You never sort the same half twice.
#
# No overlapping subproblems.
#
# ✘ DP doesn't help.
#
#
# ------------------------------------------------------------
# Example 4: Factorial
# ------------------------------------------------------------
#
# factorial(n)
# = n * factorial(n-1)
#
# Call tree:
#
#     5
#     |
#     4
#     |
#     3
#     |
#     2
#     |
#     1
#
# Every subproblem appears exactly once.
#
# No overlap.
#
# ✘ DP gives no benefit.
#
#
# ------------------------------------------------------------
# The easiest way to recognize DP
# ------------------------------------------------------------
#
# Imagine drawing the recursion tree.
#
# If you see duplicate nodes:
#
#         A
#       /   \
#      B     C
#     / \
#    C   D
#
# "C" appears twice.
#
# Repeated work.
#
# Think DP.
#
#
# If every node is unique:
#
#         A
#       /   \
#      B     C
#     / \   / \
#    D   E F   G
#
# Every problem is solved exactly once.
#
# DP won't improve anything.
#
#
# ------------------------------------------------------------
# Another way to think about it
# ------------------------------------------------------------
#
# DP is useful when recursion forms a GRAPH, not just a tree.
#
# Fibonacci:
#
#             5
#          /     \
#         4       3
#       /   \   /   \
#      3     2 2     1
#
# The recursion tree contains duplicate states (3 and 2).
#
# Memoization merges identical subproblems.
#
#
# Factorial:
#
#     5
#     |
#     4
#     |
#     3
#     |
#     2
#     |
#     1
#
# Already a straight chain.
#
# Nothing to merge.
#
#
# ------------------------------------------------------------
# Can every recursive problem be converted to Bottom-Up DP?
# ------------------------------------------------------------
#
# No.
#
# Bottom-Up DP requires:
#
# 1. Well-defined states.
# 2. A dependency order between states.
#
# Many recursive algorithms don't naturally have reusable states.
#
# Examples:
#
# - DFS on a tree
# - Tree traversals
# - Quicksort
# - Merge sort
# - Recursive directory traversal
# - Generating all permutations
# - Generating all subsets
#
# These are recursive algorithms, but they are NOT DP problems
# because they don't repeatedly solve identical subproblems.
#
#
# ------------------------------------------------------------
# Rule of Thumb
# ------------------------------------------------------------
#
# Whenever you see recursion, ask:
#
# 1. Can I define the problem using smaller subproblems?
#
#    If NO:
#        Probably not DP.
#
# 2. Do the same subproblems appear multiple times?
#
#    If NO:
#        Recursion is fine.
#        DP won't help.
#
# 3. Can I save the answer to a subproblem and reuse it later?
#
#    If YES:
#        DP is likely applicable.
#
#
# Final Summary
# ------------------------------------------------------------
#
# Recursion is a problem-solving technique.
#
# Dynamic Programming is an optimization technique for certain
# recursive (or recursively definable) problems.
#
# Recursion alone does NOT make a problem a DP problem.
#
# The defining characteristic of DP is:
#
#     Overlapping Subproblems
#
# Combined with:
#
#     Optimal Substructure
#
# If both exist, DP can usually improve an exponential recursive
# solution into a polynomial-time solution.
#
# ============================================================
"""