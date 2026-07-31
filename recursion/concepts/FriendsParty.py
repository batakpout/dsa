"""
Friends' Party!
Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only
once. Find out the total number of ways in which friends can remain single or can be paired up.

Input Format

In the function an integer N is passed as parameter.

Output Format

Return an integer representing the total no. of ways



Sample Input

3
Sample Output

4
Explanation

{1}, {2}, {3} : all single
{1}, {2,3} : 2 and 3 paired but 1 is single.
{1,2}, {3} : 1 and 2 are paired but 3 is single.
{1,3}, {2} : 1 and 3 are paired but 2 is single.

Note that {1,2} and {2,1} are considered same.
"""

r"""
Idea:

For the current friend (say Friend 1), there are only two choices:

1. Stay single:
   - Friend 1 is fixed as single.
   - Remaining (n-1) friends solve the same problem.
   - Contribution = f(n-1)

2. Pair with someone:
   - Friend 1 can pair with any of the remaining (n-1) friends.
   - After choosing the partner, both are fixed and removed.
   - Remaining (n-2) friends solve the same problem.
   - Each partner choice gives f(n-2) arrangements.
   - Since there are (n-1) partner choices,
     Contribution = (n-1) * f(n-2)

The two cases are mutually exclusive (OR), so we add them:

    f(n) = f(n-1) + (n-1) * f(n-2)

Recursion repeats the same logic on the remaining friends.
Friend 1 is chosen only to start the recursion; in the recursive call,
the "first remaining friend" plays the same role.
"""

"""
With this recurrence, you'll never reach n == 0
because there is one way to arrange zero friends: do nothing (the empty arrangement). F(0) = 1
"""

r"""
Why is f(0) = 1 instead of 0?

f(n) counts the number of valid arrangements, NOT the number of friends.

When n = 0, there are no friends to arrange.
There is exactly one valid arrangement: the empty arrangement {}.
Nobody is single, nobody is paired, and no rules are violated.

Therefore:
    f(0) = 1

This mathematical base case also makes the recurrence work naturally:
    f(n) = f(n-1) + (n-1) * f(n-2)

Example:
    f(2) = f(1) + 1 * f(0)
         = 1 + 1
         = 2
"""

"""
Time: (O(2^n)) (many overlapping recursive calls)
Auxiliary Space: (O(n)) (recursion stack)
This can later be optimized to (O(n)) time using memoization or dynamic programming.
"""


def friends_party(n) -> int:
    if n <= 2:
        return n
    return friends_party(n - 1) + ((n - 1) * friends_party(n - 2))


if __name__ == "__main__":
    n = int(input("enter total friends: "))
    print(friends_party(n))
