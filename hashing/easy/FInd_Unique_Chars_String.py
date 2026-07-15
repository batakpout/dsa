# LC easy: 387. First Unique Character in a String

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1



Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

"""
Complexity
* Time: O(n)
    * One pass to count frequencies.
    * One pass to find the first unique character.
* Space: O(1) for this problem because there are only 26 lowercase English letters
 (or O(k) where k is the number of distinct characters in a more general setting).
"""


def find_unique_chars(s: str):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


if __name__ == "__main__":
    s = input()
    print(find_unique_chars(s))
