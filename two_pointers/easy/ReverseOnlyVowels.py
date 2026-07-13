# LC 345 Easy, Reverse Vowels of a String
"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"

Output: "holle"


Example 2:

Input: s = "leetcode"

Output: "leotcede"

Example 3:

Input: s = "apple"

Output: "eppla"

Example 4:

Input: s = "education"

Output: "odicatuen"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""

#time O(N) space O(N)
def solution(input: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s=list(input)
    left, right=0, len(s) - 1
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)

if __name__ == "__main__":
    print(solution("education"))
