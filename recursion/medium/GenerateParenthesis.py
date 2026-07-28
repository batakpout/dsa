# 22. Generate Parentheses

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""


"""
If the goal is to count the number of valid strings,DP works beautifully. 
The state is simply: dp[open][close] , try it when we pick up dp?
"""

"""
C_n= 1/n+1 C(2n, n)
for n = 3, 1/4 * C(6,4) = 1/4*20 = 5, so n=3 we get 5 valid parenthesis. So this is a sequence, n=1 => 1, n=2=> 2, 
n=3 => 5, .... these are called catalan numbers
"""

"""
Time complexity: 

Each valid string has length 2n i.e maximum height is 2n

Creating/storing that string costs O(n)
There are C_n such strings. So O(n . C_n), for large numbers 
C_n  = 4^n/[n^3/2 . sqrt(pi)] 
So O(2n. C_n) ~ O(n. C_n) =~ O(4^n/sqrt(n))

Space Complexity: O(n) for the recursion stack (excluding the output). 
Including the output list, the total space is O(2n . C_n), there are C_n nos and each number has length 2n
"""
def generate_parenthesis(n) -> list[str]:
    result = []

    def helper(open, close, output):
        if open == 0 and close == 0:
            result.append(output)
            return

        if open != 0:
            helper(open - 1, close, output + "(")
        if close > open:
            helper(open, close - 1, output + ")")

    helper(n, n, "")
    return result


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(generate_parenthesis(n))
