#lc 344. Easy Reverse String

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
#time = O(n/2) ~ O(N)
#space = O(1)

def reverse3(s: list[str]) -> list[str]:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


def reverse2(s: str) -> str:
    chars = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

def reverse(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums




if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    print(reverse(nums1))

    nums2 = [5, 20, 32, 42, 5]
    print(reverse(nums2))

    s1 = "abcde"
    print(reverse2(s1))

    s2 = "abcde"
    print(reverse2(s2))
