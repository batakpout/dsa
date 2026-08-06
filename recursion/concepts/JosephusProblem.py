"""

"""


"""
Since the numbering has rotated by k positions, converting a position from the smaller numbering back to the larger 
numbering requires adding k modulo n.
"""

"""
Josephus Problem (n = 5, k = 3)

At every recursive level:
- Left column = current indices seen by recursion.
- Right column = original person numbers.

---------------------------------------------------------
n = 5

Current Index    Original Person
------------    ---------------
0               0
1               1
2               2   <- removed
3               3
4               4

Remaining circle:
3 4 0 1

Mapping:
0 -> 3
1 -> 4
2 -> 0
3 -> 1

J(4)
---------------------------------------------------------
n = 4

Current Index    Original Person
------------    ---------------
0               3
1               4
2               0   <- removed
3               1

Remaining circle:
1 3 4

Mapping:
0 -> 1
1 -> 3
2 -> 4

J(3)
---------------------------------------------------------
n = 3

Current Index    Original Person
------------    ---------------
0               1
1               3
2               4   <- removed

Remaining circle:
1 3

Mapping:
0 -> 1
1 -> 3

J(2)
---------------------------------------------------------
n = 2

Current Index    Original Person
------------    ---------------
0               1   <- removed
1               3

Remaining circle:
3

Mapping:
0 -> 3

J(1)
---------------------------------------------------------
n = 1

Current Index    Original Person
------------    ---------------
0               3

Base case:
J(1) = 0

---------------------------------------------------------
Unwinding

J(2) = (0 + 3) % 2 = 1   -> Original Person 3
J(3) = (1 + 3) % 3 = 1   -> Original Person 3
J(4) = (1 + 3) % 4 = 0   -> Original Person 3
J(5) = (0 + 3) % 5 = 3   -> Original Person 3

Returned indices:
0 -> 1 -> 1 -> 0 -> 3

Actual winner (never changes):
Person 3

Key Idea:
The recursion never tracks the original person number.
It only tracks the winner's CURRENT POSITION in each
smaller problem. Each level has its own numbering.
(prev + k) % n converts that position back to the
previous level's numbering.
"""

"""
O(n) Time and O(n) Space
"""
def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n - 1, k) + k) % n

def josephus_problem(n: int, k: int) -> int:
    arr = list(range(1, n + 1))

    def helper(i):
        if len(arr) == 1:
            return arr[0]
        i = (i + k - 1) % len(arr)
        arr.pop(i)
        return helper(i)

    return helper(0)

if __name__ == "__main__":
    n = int(input("enter n: "))
    k = int(input("enter k: "))
   # print(josephus_problem(arr, n, k))
    print(josephus(n, k) + 1)
