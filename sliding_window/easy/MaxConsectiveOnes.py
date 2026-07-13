#LC 485 Easy
"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2



Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""

#time=O(n), space=O(1)
def maximum_consecutive_ones(nums: list[int]) -> int:
    current_length = 0
    max_length = 0
    for num in nums:
        if num == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length=0

    return max(max_length, current_length) # max here to cover if all are 1's in array


if __name__ == "__main__":
    nums1 = [1, 1, 0, 1, 1, 1]
    print(maximum_consecutive_ones(nums1))

    nums2 = [1, 0, 1, 1, 0, 1]
    print(maximum_consecutive_ones(nums2))
