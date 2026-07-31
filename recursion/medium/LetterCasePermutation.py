#784. Letter Case Permutation

"""

Topics
premium lock icon
Companies
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]


Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""


"""
Time Complexity:
(n) = length of the string.
(k) = number of alphabetic characters (letters).
Only the letters branch into two recursive calls. Digits have only one choice.

There are (2^k) leaf nodes (valid permutations).
Each output string has length (n), and building it using "output + input_str[0]" creates a new string, which costs
 (O(n)) over the full path.
So, O(n.2^k)

Space Complexity: 
auxillary: The maximum recursion depth is O(n)
total with result = O(n * 2^k), there are 2^k strings and building each string is of length n.
"""

def letter_case_permutation2(s: str) -> list[str]:
    result = []

    def helper(output, input_str):
        if len(input_str) == 0:
            result.append(output)
            return
        if input_str[0].isdigit():
            helper(output + input_str[0], input_str[1:])
        else:
            helper(output + input_str[0], input_str[1:])
            helper(output + input_str[0].swapcase(), input_str[1:])

    helper("", s)
    return result

if __name__ == "__main__":
    s = input("enter a string: ")
    # permutation_with_spaces(s[0], s[1:])
    #permutation_with_case_change("", s)
    print(letter_case_permutation2(s))
