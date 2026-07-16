# LC 383 Ransom Note

"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "abcc", magazine = "aaabbbc"
Output: false

Example 4:
Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

"""
Time Complexity

* O(m + n)
    * m = len(magazine)
    * n = len(ransomNote)
   = O(N)
Space Complexity
* O(1) because there are only 26 lowercase English letters.
* More generally, O(k) where k is the number of distinct characters
"""


def ransom_note_check(ransom_note, magazine):
    freq = {}
    for ch in magazine:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in ransom_note:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True

# faster but works only for alphabets, exactly same as anagram check
def ransom_note_check2(s: str, t: str) -> bool:
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
    result = ransom_note_check(s, t)

    print(result)
