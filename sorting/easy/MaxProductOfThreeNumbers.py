#LC 628 Easy Maximum Product of Three Numbers

"""

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
Example 1:

Input = nums = [-10, -8, -3, 1, 4, 9]
output not 36 but maximum is -10 * -8 = 80 * 9 = 720

Input: nums = [-1,-2,-3]
Output: -6


Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000

"""
"""
* Time Complexity: O(n log n)
* Space Complexity: O(1) (Python’s sort uses some auxiliary memory internally, but in interview discussions it’s typically considered in-place).
"""
def max_product_of_three_numbers(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    product1 = nums[n-1] * nums[n-2] * nums[n-3]
    product2 = nums[0] * nums[1] * nums[n-1]
    return max(product1, product2)

if __name__ == "__main__":
    nums1 = []
    res1 = max_product_of_three_numbers()