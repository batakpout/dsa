# LC 242. easy Valid Anagram

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

"""
listen  → silent

we need to keep an eye on these cases:
1. s = "aab" and t = "abb"
map {a:2, b:1}
and
2. s="ab" and t = "aa"
map = {a:1, b:1}
"""

"""
Time Complexity: O(n)
Space Complexity: O(1) for this LeetCode problem because the strings contain only lowercase English letters, so the 
hash map stores at most 26 keys. (More generally, it is O(k) where k is the number of distinct characters.)
"""


# this works for Unicode characters also.
def is_anagram(s: str, t: str):
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:  # check examples 2 in starting comment
            return False
        freq[ch] -= 1

    for c in freq.values():
        if c != 0:
            return False
    return True


# faster but works only for alphabets
def is_anagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for ch in t:
        index = ord(ch) - ord('a')
        if count[index] == 0:
            return False
        count[index] -= 1

    return True


if __name__ == "__main__":
    s = input("Enter s: ")
    t = input("Enter t: ")
    result = is_anagram2(s, t)

    print(result)
