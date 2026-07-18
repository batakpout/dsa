"""
Tiling Problem (Recursion - Understanding the Recurrence)

Problem
-------
Given:
- A floor of size N x M
- Tiles of size 1 x M

Each tile can be placed:
1. Horizontally (1 x M)
2. Vertically (M x 1)

Goal:
Count the total number of ways to completely tile the floor.


Subproblem
----------
Let:

    Ways(N, M)

represent the number of ways to tile an N x M board.

Since M (the width of the board or the tile length) never changes during
recursion, we often write:

    Ways(N)


How do we build the recurrence?
-------------------------------

Look ONLY at the first row of the current board.

There are only TWO possible ways to completely cover the first row.

-------------------------------------------------------
Case 1 : Place one horizontal tile
-------------------------------------------------------

Current board

    N x M

Place one horizontal tile:

    ===

This consumes exactly ONE row.

Remaining board:

    (N - 1) x M

Number of ways:

    Ways(N - 1)


-------------------------------------------------------
Case 2 : Place vertical tiles
-------------------------------------------------------

To cover the first row vertically, every column must contain one
vertical tile.

Example (M = 3)

    ABC
    ABC
    ABC
    ...

This consumes exactly M rows.

Remaining board:

    (N - M) x M

Number of ways:

    Ways(N - M)


Recurrence
----------

Ways(N)
=
Ways(N - 1)
+
Ways(N - M)


Base Cases
----------

1. If M == 1

A 1x1 tile looks the same after rotation.

There is only one possible tiling.

    Ways(N) = 1


2. If N < M

There are not enough rows to place a vertical tile.

Only horizontal placement is possible.

Example:

    N = 2, M = 3

    ===
    ===

Only one arrangement.

    Ways(N) = 1


3. If N == M

Two possibilities exist.

Horizontal:

    ===
    ===
    ===

Vertical:

    |||
    |||
    |||

Therefore,

    Ways(N) = 2

4. N <=0 and M<=0 doesn't make any sense so invalid input

5. N == M == 1, will return 1 as M==1 is a base case.

6. for all other case we will cover either in base case or recurrence

Important Idea
--------------

We are NOT saying:

    "Place horizontal first, then vertical."

Instead, we partition ALL valid tilings into two disjoint groups.

Group 1:
    Tilings whose first row is covered horizontally.

Group 2:
    Tilings whose first row is covered vertically.

Since every valid tiling belongs to exactly one of these groups,
the total number of tilings is

    Ways(N)
    =
    Ways(N - 1)
    +
    Ways(N - M)

This is why the recurrence works.
"""


def ways(n, m):
    if m == 1:
        return 1

    if n < m:
        return 1

    if n == m:
        return 2

    return ways(n - 1, m) + ways(n - m, m)


def main():
    test_cases = [
        (1, 1, 1),
        (2, 1, 1),
        (3, 1, 1),
        (1, 2, 1),
        (2, 2, 2),
        (3, 2, 3),
        (4, 2, 5),
        (4, 3, 3),
        (5, 3, 4),
    ]

    print(f"{'N':<3} {'M':<3} {'Expected':<10} {'Program':<10}")
    print("-" * 35)

    for n, m, expected in test_cases:
        result = ways(n, m)
        print(f"{n:<3} {m:<3} {expected:<10} {result:<10}")


if __name__ == "__main__":
    main()
