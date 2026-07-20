# LC 20 Valid Parenthesis
"""

    LC: 20; E Valid Parentheses
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false


"""

"""
* Time: O(N)
    * You scan the string exactly once.
    * Each character is pushed and popped at most once.
* Space: O(N)
    * In the worst case (e.g., "((((((("), the stack stores all opening brackets.
"""



def is_matching(c1: str, c2: str) -> bool:
    return (
            (c1 == '{' and c2 == '}') or
            (c1 == '[' and c2 == ']') or
            (c1 == '(' and c2 == ')')
    )


def is_balanced(s: str) -> bool:
    stack = []
    for ch in s:
        if ch == '{' or ch == '[' or ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            elif not is_matching(stack[-1], ch):
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    user_input = input("enter:")
    result = is_balanced(user_input)
    print(result)
