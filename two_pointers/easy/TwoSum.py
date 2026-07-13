# Approach:- two pointer from both sides, one pointer from left other from right
# LeetCode 1 , two sums

"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

"""
Time:
    Sort      = O(n log n)
    Iterate   = O(n)
    -----------------
    Total     = O(n log n + n)
    When one term grows much faster than the other, we keep only the dominant term.
    So, O(n log n + n) = O(n log n)
Space = O(n) for algorithms like mergesort that need extra memory, else O(1) if sorting in place e.g heap sort with TC also  O(n log n)
"""
def using_two_pointer(target:int, nums: list[int])->list[int]:
    left = 0
    right = len(list)-1
    sorted(nums)
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return [-1,-1]



if __name__ == "__main__":
    nums1 = [2, 3, 6, 7, 11, 9, 16]
    target1 = 15
    print(using_two_pointer(target1, nums1))

    nums2 = [3, 21, 4, 2, 4]
    target2 = 6
    print(using_two_pointer(target2, nums2))

    nums3 = [3, 32,2,1,]
    target3 = 8
    print(using_two_pointer(target3, nums3))