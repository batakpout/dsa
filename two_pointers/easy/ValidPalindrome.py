# LC Easy 125 Valid Palindrome

"""
Alphanumeric characters are a combined set of letters and numbers. They include all 26 letters of the English alphabet
 (A-Z, both uppercase and lowercase) and all 10 Arabic numerals (0-9)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def naive(s: str) -> bool:
    new_str = ""
    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]


# O(N) time and O(1) space
# two pointers from both ends
def optimized(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alpha_numeric(s[l]): #l<r used because when s = "!!!"
            l += 1

        while r > l and not alpha_numeric(s[r]): #r>l used e.g s="a!!!" ??
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1
    return True


def alpha_numeric(c: str) -> bool:
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))





if __name__ == "__main__":
    print(naive("A man, a plan, a canal: Panama"))
    print(naive("race a car"))

    print(optimized("A man, a plan, a canal: Panama"))
    print(optimized("race a car"))
    print(optimized("a!!!"))
