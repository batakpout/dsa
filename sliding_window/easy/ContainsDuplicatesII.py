# LC Easy 219
"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
1 -> index 0
1 -> index 3
and
abs(3 - 0) = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
1 -> index 2
1 -> index 3
1 <= 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
1 at indices 0 and 3
2 at indices 1 and 4
3 at indices 2 and 5
Output: false

"""
"""
Set operations (in, add, remove) are O(1) on average.
Space = O(min(n, k))
time = O(n)
This is why the sliding-window solution is considered the optimal solution for LeetCode 219 (Contains Duplicate II): 
it achieves the same O(n) time while reducing space from O(n) to O(k).
"""


def contains_duplicates(K: int, nums: list[int]) -> bool:
    L = 0
    window = set()
    for R in range(len(nums)):
        if R - L > K:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1, 2, 3, 1, 2, 1, 3]
    k1 = 2
    print(contains_duplicates(k1, nums1))

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(contains_duplicates(k, nums))
