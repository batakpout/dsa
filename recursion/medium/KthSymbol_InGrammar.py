# LC 779 K-th Symbol in Grammar, Medium

"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at
the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.



Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01
Example 3:

Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01


Constraints:

1 <= n <= 30
1 <= k <= 2n - 1
"""


"""
we never make two recursive calls. Each call makes exactly one recursive call.

The recursion goes like this:
n = 5
↓
n = 4
↓
n = 3
↓
n = 2
↓
n = 1
So O(N)
Space: recursive stack O(N)
"""
def kth_grammar_1(n: int, k: int) -> int:
    if n == 1 or k == 1:
        return 0
    else:
        mid = 2 ** (n - 1) // 2
        if k <= mid:
            return int(kth_grammar_1(n - 1, k))
        else:
            return int(not kth_grammar_1(n - 1, k - mid))  # not 0 means not false and not 1 means not true


def kth_grammar_2(n: int, k: int) -> int:
    if n == 1 or k == 1:
        return 0
    else:
        mid = 1 << (
                    n - 2)  # 1<<2 means shift 1 by 2 bits gives 4, so for n=4 we need mid as 8/2 = 4 so 1 << (4-2) , shift 1 by 2 i.e 4
        if k <= mid:
            return kth_grammar_2(n - 1, k)
        else:
            return 1 - int(not kth_grammar_2(n - 1, k - mid))  # if 0 then 1-0 is 1 and if 1 then 1-1 is 0


if __name__ == "__main__":
    test_cases = [
        (1, 1, 0),
        (2, 1, 0),
        (2, 2, 1),
        (3, 1, 0),
        (3, 2, 1),
        (3, 3, 1),
        (3, 4, 0),
        (4, 5, 1),
        (4, 8, 1),
        (5, 16, 0),
    ]

    print("Testing kth_grammar_1")
    for n, k, expected in test_cases:
        result = kth_grammar_1(n, k)
        print(f"n={n}, k={k} -> Expected: {expected}, Got: {result}")

    print("\nTesting kth_grammar_2")
    for n, k, expected in test_cases:
        result = kth_grammar_2(n, k)
        print(f"n={n}, k={k} -> Expected: {expected}, Got: {result}")