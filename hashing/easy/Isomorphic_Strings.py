# LC 205. Easy: Isomorphic Strings

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true



Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""

"""
Problem:
Determine whether there is a one-to-one mapping between the characters of s and t.
Each character in s must always map to the same character in t, and no two
different characters in s can map to the same character in t.

Also s is isomorphic to t and vice-versa

Use two hash maps to ensure bijective character mapping between strings.

We use two hash maps:
1. s_to_t : maps characters from s -> t
2. t_to_s : maps characters from t -> s

Example (no repeated characters):
s = "abc"
t = "xyz"

s_to_t = {a:x, b:y, c:z}
t_to_s = {x:a, y:b, z:c}

Both maps are consistent, so return True.
========================================================================================================================
Example:
s = "paper"
t = "title"

Pairs:
(p,t), (a,i), (p,t), (e,l), (r,e)

s_to_t:
p -> t
a -> i
e -> l
r -> e

t_to_s:
t -> p
i -> a
l -> e
e -> r

Notice that "e -> l" (forward map) and "l -> e" (reverse map) are NOT a conflict.
The maps are checked independently. A conflict occurs only if the SAME KEY in the
SAME MAP tries to map to a different value.
========================================================================================================================
Example (conflicting forward mapping):

s = "foo" t = "bar"

Pairs: (f,b), (o,a), (o,r)
s_to_t: f -> b o -> a
o -> r    <-- conflict (same key, different value)

t_to_s: b -> f a -> o
return False
========================================================================================================================
Example (conflicting reverse mapping):
s = "bar" t = "foo"
Pairs: (b,f), (a,o), (r,o)
s_to_t: b -> f a -> o r -> o

t_to_s: f -> b o -> a
o -> r    <-- conflict (same key, different value)

The character 'o' in t first maps back to 'a' and later tries to map back to 'r'.

Two different characters in s ('a' and 'r') cannot map to the same character 'o' in t,

so return False.
========================================================================================================================
s = "foo"
t = "baa"
:returns True
========================================================================================================================
Conflict example:
s = "ab"
t = "aa"

After first pair:
s_to_t = {a:a}
t_to_s = {a:a}

Second pair: (b,a)

Forward map:
b is new -> OK

Reverse map:
'a' already maps to 'a', but now it would need to map to 'b'.

t_to_s:
a -> a
a -> b   <-- conflict (same key, different value)

Hence return False.
"""

"""
Time-complexity: O(N)
Space-complexity: O(N) + O(N) = O(N)
"""


def iso_strings(s, t) -> bool:
    if len(s) != len(t):
        return False

    m1, m2 = {}, {}  # m1 forward mapping, m2 reverse mapping

    for ch1, ch2 in zip(s, t):
        if ((ch1 in m1 and m1[ch1] != ch2) or
                (ch2 in m2 and m2[ch2] != ch1)):
            return False
        m1[ch1] = ch2
        m2[ch2] = ch1
    return True


if __name__ == "__main__":
    s = input("Enter s: ")
    t = input("Enter t: ")
    result = iso_strings(s, t)

    print(result)
